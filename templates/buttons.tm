<!-- Buttons.tm start -->

<div class="div pad {{class}}">
{{label}}

<div id="{{button_list_id}}" class="btn-group btn-group-justified " data-toggle="buttons" >


{{#buttons_list}}
  <label class="btn btn-primary btn-md" id="{{name}}">
<input type="radio" name="{{button_radios_name}}"  value="{{name}}">{{display}}</input>
  </label>
{{/buttons_list}}

{{#checkboxes_list}}
  <label class="btn btn-primary btn-md" id="{{name}}">
<input type="checkbox" name="{{button_radios_name}}"  value="{{name}}">{{display}}</input>
  </label>
{{/checkboxes_list}}

</div>
</div>
{{#check_all}}

<div id="{{check_all_id}}_div" class="blue">
	<input type="button" id="{{check_all_id}}" value="Check All">
	</input>
</div> <!-- check_all -->

{{/check_all}}

<!-- Buttons.tm end-->
