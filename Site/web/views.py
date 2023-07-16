from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return HttpResponse('''<html>
<title>Home</title>
<head>
<style>
h1{
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}
</style>
<body>
    <h1>"Be yourself; everyone else is already taken"</h1>
    {%}
</body> 
</head>
</style>           
</html>''')