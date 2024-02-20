import os
import json

import multiprocessing as mp
import sys

import logging
from datetime import datetime


def counters(json_line):
    json_array = {}
    counters_columns = []
    json_counters = json_line['counters']

    for counter in json_counters:
        if counter not in counters_columns:
            counters_columns.append(counter)
        json_array[counter] = json_counters[counter]['count']
    return json_array, counters_columns


def gauges(json_line):
    json_array = {}
    gauge_columns = []
    json_gauges = json_line['gauges']
    for gauge in json_gauges:
        if gauge not in gauge_columns:
            gauge_columns.append(gauge)
        json_array[gauge] = json_gauges[gauge]['value']
    return json_array, gauge_columns


def timers(json_line):
    json_array = {}
    timer_columns = []
    json_timers = json_line['timers']
    for timer in json_timers:
        for timer_subcolumn in json_timers[timer]:
            # if timer_subcolumn not in ("duration_units", "rate_units","m15_rate","m1_rate",
            #                            "m5_rate","mean_rate","stddev"):
            if timer_subcolumn in ("max", "mean"):
                comb_timer_column = timer + "." + timer_subcolumn
                if comb_timer_column not in timer_columns:
                    timer_columns.append(comb_timer_column)
                json_array[comb_timer_column] = "{0:.2f}".format(json_timers[timer][timer_subcolumn])
    return json_array, timer_columns


def histograms(json_line):
    json_array = {}

    histogram_columns = []
    json_histograms = json_line['histograms']
    for histogram in json_histograms:
        for histogram_subcolumn in json_histograms[histogram]:
            if histogram_subcolumn in ("max", "mean"):
                comb_histogram_column = histogram + "." + histogram_subcolumn
                if comb_histogram_column not in histogram_columns:
                    histogram_columns.append(comb_histogram_column)

                json_array[comb_histogram_column] = "{0:.2f}".format(json_histograms[histogram][histogram_subcolumn])
    return json_array, histogram_columns


def process_file(path, filename):
    logging.debug("{} is starting".format(filename))
    logging.debug(datetime.now())

    json_array = {}
    json_line = None
    current_time = None

    temp_counter_arrays = []
    temp_gauge_arrays = []
    temp_histogram_arrays = []
    temp_timer_arrays = []

    file_counters_columns = ['date']
    file_timer_columns = ['date']
    file_gauge_columns = ['date']
    file_histogram_columns = ['date']

    with open(path + "/" + filename, 'r') as instrumentation_file:
        for line in instrumentation_file:

            if "2" == line[:1]:
                try:
                    if json_line is not None:
                        json_line = json.loads(json_line)
                        json_array['date'] = current_time

                        json_array['counters'] = {}
                        json_array['gauges'] = {}
                        json_array['timers'] = {}
                        json_array['histograms'] = {}

                        temp_counters, temp_counters_columns = counters(json_line)
                        json_array['counters'] = temp_counters
                        json_array['counters']['date'] = json_array['date']

                        # temp_histograms, temp_histograms_columns = histograms(json_line)
                        # json_array['histograms'] = temp_histograms
                        # json_array['histograms']['date'] = json_array['date']
                        #
                        # temp_gauges, temp_gauges_columns = gauges(json_line)
                        # json_array['gauges'] = temp_gauges
                        # json_array['gauges']['date'] = json_array['date']
                        #
                        # temp_timers, temp_timers_columns = timers(json_line)
                        # json_array['timers'] = temp_timers
                        # json_array['timers']['date'] = json_array['date']

                        temp_counter_arrays.append(json_array['counters'])
                        # temp_timer_arrays.append(json_array['timers'])
                        # temp_gauge_arrays.append(json_array['gauges'])
                        # temp_histogram_arrays.append(json_array['histograms'])

                        file_counters_columns = list(set(file_counters_columns + temp_counters_columns))

                        logging.info (temp_counter_arrays)
                        # file_histogram_columns = list(set(file_histogram_columns + temp_histograms_columns))
                        # file_gauge_columns = list(set(file_gauge_columns + temp_gauges_columns))
                        # file_timer_columns = list(set(file_timer_columns + temp_timers_columns))

                    met_time = line.split(',', 1)[0]
                    current_time = met_time
                    json_line = ""
                    json_array = {}

                except Exception as e:
                    logging.debug("{}, {}, exception={}".format(filename, line, e))
                    met_time = line.split(',', 1)[0]
                    current_time = met_time
                    json_line = ""
                    json_array = {}
            else:
                json_line += " " + line

    logging.debug("{} is done".format(filename))
    logging.debug(datetime.now())

    return temp_counter_arrays, temp_histogram_arrays, temp_gauge_arrays, temp_timer_arrays, file_counters_columns, \
           file_histogram_columns, file_gauge_columns, file_timer_columns


def metrics(async_execution=0):
    counters_columns = ['date']
    timer_columns = ['date']
    gauge_columns = ['date']
    histogram_columns = ['date']

    path = sys.argv[1]

    counter_arrays = []
    gauge_arrays = []
    timer_arrays = []
    histogram_arrays = []

    matched_filenames = []
    for filename in os.listdir(path):

        if filename.startswith("oozie-instrumentation"):
            matched_filenames.append(filename)
    results = []
    if async_execution is 1:
        pool = mp.Pool(4)
        results = [pool.apply_async(process_file, args=(path, matched_filename)) for matched_filename in
                   matched_filenames]
        pool.close()
        pool.join()

        logging.debug("All files are done")
        logging.debug(datetime.now())

        for result in results:
            temp_counter_arrays, temp_histogram_arrays, temp_gauge_arrays, temp_timer_arrays, file_counters_columns, \
            file_histograms_columns, file_gauges_columns, file_timers_columns = result.get()

            counters_columns = list(set(counters_columns + file_counters_columns))
            histogram_columns = list(set(histogram_columns + file_histograms_columns))
            gauge_columns = list(set(gauge_columns + file_gauges_columns))
            timer_columns = list(set(timer_columns + file_timers_columns))

            counter_arrays.extend(temp_counter_arrays)
            gauge_arrays.extend(temp_gauge_arrays)
            timer_arrays.extend(temp_timer_arrays)
            histogram_arrays.extend(temp_histogram_arrays)

    else:
        for matched_filename in matched_filenames:
            result = process_file(path, matched_filename)
            results.append(result)

        for temp_counter_arrays, temp_histogram_arrays, temp_gauge_arrays, temp_timer_arrays, file_counters_columns, \
            file_histograms_columns, file_gauges_columns, file_timers_columns in results:
            counters_columns = list(set(counters_columns + file_counters_columns))
            histogram_columns = list(set(histogram_columns + file_histograms_columns))
            gauge_columns = list(set(gauge_columns + file_gauges_columns))
            timer_columns = list(set(timer_columns + file_timers_columns))

            counter_arrays.extend(temp_counter_arrays)
            gauge_arrays.extend(temp_gauge_arrays)
            timer_arrays.extend(temp_timer_arrays)
            histogram_arrays.extend(temp_histogram_arrays)
    

if __name__ == '__main__':
    logging.basicConfig(filename="output.log", level=logging.DEBUG)
    startTime = datetime.now()
    logging.debug(startTime)
    metrics(1)
    logging.debug(datetime.now() - startTime)
