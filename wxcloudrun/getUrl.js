
function getQueryVariable(variable) {
    var query = window.location.search.substring(1);
    var vars = query.split("&");
    for (var i = 0; i < vars.length; i++) {
        var pair = vars[i].split("=");
        if (pair[0] == variable) {
            return pair[1];
        }
    }
    return (false);
}
function getopenid(url){
    var xmlhttp=new XMLHttpRequest();
    var type="GET";//方法
    xmlhttp.open(type,url);//方法，接口，异步
    xmlhttp.send();//发送请求
    xmlhttp.onreadystatechange=function(){
    if(xmlhttp.status==200&&xmlhttp.readyState==4){
        var result=JSON.parse(xmlhttp.response); //获取到的json数据
  }
    console.log(result)
  }
}
function main(){
  const jsdom = require("jsdom");
  const { JSDOM } = jsdom;
  const dom = new JSDOM(`<!DOCTYPE html><p>Hello world</p>`);
  window = dom.window;
  document = window.document;
  XMLHttpRequest = window.XMLHttpRequest;
  console.log("1")
  if (window.location.search.indexOf('code=')==-1){
      const baseurl='https://open.weixin.qq.com/connect/oauth2/authorize'
      const redirect_uri=window.location.href
      const state='1234'
      const appid='wx264ea0f7e61d1723'
      location=(`${baseurl}?appid=${appid}$redirect_uri=${redirect_uri}&response_type=code&scope=snsapi_base&state=${state}#wechat_redirect`)
      window.location.href= `${baseurl}?appid=${appid}&redirect_uri=${redirect_uri}&response_type=code&scope=snsapi_base&state=${state}#wechat_redirect`
    }
  
  if(getQueryVariable('code')){
    var code= getQueryVariable('code')
    document.write("id: "+code)
    console.log(code)
    const appid='wx264ea0f7e61d1723'
    const secret="0627dc277cfe7f3bd883a0d0ad4c3aec"
    const baseurl_getopenid ="https://api.weixin.qq.com/sns/oauth2/access_token"
    var url= `${baseurl_getopenid}?appid=${appid}&secret=${secret}&code=${code}&grant_type=authorization_code`
    // getopenid(url) 
    console.log(url)
    return url
  }
}

