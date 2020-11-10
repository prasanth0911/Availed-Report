from django.shortcuts import render
from .models import Unknown

import psycopg2


# Create your views here.


from django.http import HttpResponse

def availed1(request):
    html = """<!DOCTYPE html>
<html>
<head>
<title>Project</title>
<link rel="stylesheet" type="text/css" href="C:/Users/Prashanth/Desktop/HTML/ProjectStyles.css">
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
<script src="http://code.jquery.com/jquery-1.9.1.min.js"></script>
<script src ="https://cdn.datatables.net/1.10.22/js/jquery.dataTables.min.js"></script>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
<script type="text/javascript">
  
  $(document).ready(function () {
  $('#BasicTable').DataTable({
    "pagingType": "simple_numbers" // "simple" option for 'Previous' and 'Next' buttons only
  });
  $('.dataTables_length').addClass('bs-select');
});

</script>
<script type="text/javascript">
  $(document).ready(function() {
  $('[data-toggle="toggle"]').change(function(){
    $(this).parents().next('.hide').toggle();
  });
});
</script>
</head>

<body>
<div>
<h1>Generate Report for Availed and Non Availed Shutdown Requests</h1>
</div>
<script type="text/javascript">

var Intial_list=[[1234,5678,"Element1","19-08-2020","25-09-2020",1],[1235,5679,"Element2","19-08-2020","25-09-2020",1],
[null,5680,"Element3","19-08-2020","25-09-2020",0],[1236,5678,"Element4","19-08-2020","25-09-2020",1],
[1237,5678,"Element1","19-08-2020","25-09-2020",1],[null,5683,"Element2","19-08-2020","25-09-2020",0],
[1234,5678,"Element1","19-08-2020","25-09-2020",1],[1235,5679,"Element2","19-08-2020","25-09-2020",1],
[null,5680,"Element3","19-08-2020","25-09-2020",0],[1236,5678,"Element4","19-08-2020","25-09-2020",1],
[1237,5678,"Element1","19-08-2020","25-09-2020",1],[null,5683,"Element2","19-08-2020","25-09-2020",0],
[1234,5678,"Element1","19-08-2020","25-09-2020",1],[1235,5679,"Element2","19-08-2020","25-09-2020",1],
[null,5680,"Element3","19-08-2020","25-09-2020",0],[1236,5678,"Element4","19-08-2020","25-09-2020",1],
[1237,5678,"Element1","19-08-2020","25-09-2020",1],[null,5683,"Element2","19-08-2020","25-09-2020",0],
[1234,5678,"Element1","19-08-2020","25-09-2020",1],[1235,5679,"Element2","19-08-2020","25-09-2020",1],
[null,5680,"Element3","19-08-2020","25-09-2020",0],[1236,5678,"Element4","19-08-2020","25-09-2020",1],
[1237,5678,"Element1","19-08-2020","25-09-2020",1],[null,5683,"Element2","19-08-2020","25-09-2020",0],
[1234,5678,"Element1","19-08-2020","25-09-2020",1],[1235,5679,"Element2","19-08-2020","25-09-2020",1],
[null,5680,"Element3","19-08-2020","25-09-2020",0],[1236,5678,"Element4","19-08-2020","25-09-2020",1],
[1237,5678,"Element1","19-08-2020","25-09-2020",1],[null,5683,"Element2","19-08-2020","25-09-2020",0],
[1234,5678,"Element1","19-08-2020","25-09-2020",1],[1235,5679,"Element2","19-08-2020","25-09-2020",1],
[null,5680,"Element3","19-08-2020","25-09-2020",0],[1236,5678,"Element4","19-08-2020","25-09-2020",1],
[1237,5678,"Element1","19-08-2020","25-09-2020",1],[null,5683,"Element2","19-08-2020","25-09-2020",0]]





<div id="Availed"><h2 class="Avld">
<button onclick="approve(1)">Availed Report</button>
</h2></div>
<div id="Unknown"><h2 class="Unknwn">
<button onclick="approve(0)">Unknown Report</button>
</h2></div>
<div id="my_table"></div>
</body>
</html>
"""
    return HttpResponse(html)


def home(request):
    return HttpResponse("This is home page")



def example(request):
    data=Unknown.objects.raw('select * from calc_unknown')
    return render(request, 'example.html', {'items' : data})


def availed(request):

    data=Unknown.objects.raw('select * from calc_unknown where outageid!=0  order by startdate asc')
    return render(request,'Availed.html',{'items':data})

def  unknown(request):
    data=Unknown.objects.raw('select * from calc_unknown order by startdate desc')
    return render(request,'Unknown.html',{'items':data})




