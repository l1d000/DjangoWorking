var xhr = '';
if (window.XMLHttpRequest) {
    xhr = new window.XMLHttpRequest();
} else {
    xhr = new ActiveXObject('Microsoft.XMLHttp');
}

function myfun() {
    var pg = document.getElementById('pg');
    setInterval(function(e) {
        //   draw();
        var xhr = '';
        if (window.XMLHttpRequest) {
            xhr = new window.XMLHttpRequest();
        } else {
            xhr = new ActiveXObject('Microsoft.XMLHttp');
        }

        xhr.open('get', 'get_progress', true);
        xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
        xhr.send('memberId=' + "111" + '&&password=' + "2222");
        xhr.onreadystatechange = function() {
            // readyState: 
            //     0: 请求未初始化
            //                 1: 服务器连接已建立
            //                 2: 请求已接收
            //                 3: 请求处理中
            //                 4: 请求已完成，且响应已就绪
            //             status:
            //                 200: 'ok'
            //                 404: 未找到页面或接口
            //                 xhr.responseText: 后端返回的数据
            if (xhr.readyState == 4 && xhr.status == 200) {
              //  document.getElementById('box').innerHTML = xhr.responseText + "%";

                var json = JSON.parse(xhr.responseText);
              //  console.log(json);
                document.getElementById('progressbar_s').style.width = json.progressbar_s + "%";
                document.getElementById('progressbar_b').style.width = json.progressbar_b + "%";

            }

        }
    },
    5000);

}
window.onload = myfun;
