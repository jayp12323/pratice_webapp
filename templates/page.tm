

<!-- template.tm starts here -------------------------------------------------------------------->

<html>
<head>
<meta charset="utf-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel='shortcut icon' type='image/x-icon' href=' /static/favicon.ico' />

	<!-- Bootstrap core CSS -->
<link href="/static/css/bootstrap-min.css" rel="stylesheet">
<link href="https://cdnjs.cloudflare.com/ajax/libs/select2/4.0.6-rc.0/css/select2.min.css" rel="stylesheet" />

<link href="/static/css/sticky-footer-navbar.css" rel="stylesheet">
<link href="/static/css/template.css" rel="stylesheet">

<!-- extra css files starts here -------------------------------------------------------------------->

	{{#css}}
		<style type="text/css" media="all">@import " /static/css/{{name}}";</style>
	{{/css}}

<!-- extra css files starts here -------------------------------------------------------------------->

</head>
<body>

<!-- navigation buttons starts here -------------------------------------------------------------------->

{{{main_nav}}}

<!-- navigation buttons ends here -------------------------------------------------------------------->

<div id="left_col" class="container col-md-{{lsize}}">
{{{left_side}}}
</div>

<!-- main page body starts here -------------------------------------------------------------------->
<div id="body_col" class="container col-md-{{bsize}} center-block">
{{{body}}}
</div>

<!-- main page body ends here -------------------------------------------------------------------->

<div id="right_col" class="container col-md-{{rsize}}">
{{{right_side}}}
</div>


<script src="https://code.jquery.com/jquery-3.3.1.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js" integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49" crossorigin="anonymous"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js" integrity="sha384-ChfqqxuZUCnJSK3+MXmPNIyE6ZbWh2IMqE241rYiqJxyMiZ6OW/JmZQ5stwEULTy" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/select2/4.0.6-rc.0/js/select2.min.js"></script>

<!-- extra javascript files starts here -------------------------------------------------------------------->

	{{#javascripts}}
		<script src="/static/js/{{name}}"></script>
	{{/javascripts}}
<!-- extra javascript files ends here -------------------------------------------------------------------->

<!-- main page body ends here -------------------------------------------------------------------->
</body>


<!-- template.tm ends here -------------------------------------------------------------------->
