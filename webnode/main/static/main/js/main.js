$(document).ready(function(){
  today = new Date();
  $('#time').append(today.getFullYear() + '-' + (today.getMonth()+1) + '-' + today.getDate() + ' ' + today.getHours() + '時' + today.getMinutes() + '分');
});