
$(document).ready(function() {
  $('#id_cod_solicitud').change(function() {
    $.ajax({
      type: 'POST',
      url: "{% url get_template_info %}",
      data: {'cod_solicitud': $('#id_cod_solicitud').val()},
      success: function(data, _status) {
        $('#id_apellido_1').val(data.apellido_1);

      },
      dataType: "json"
    });               
  });
});