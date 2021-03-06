---
layout: post
title: Java send http get post request
categories: java
tags: [java, http]
---

最近，公司的一个项目需要拿到第三方项目的数据，我们解决的大致思路就是Java发送HTTP GET POST请求，得到页面数据之后，用jsoup进行解析，然后入库。由于这个第三方项目需要登录，所以，我们第一次登陆请求进去之后，需要记录下cookie，下次发送请求的时候，直接把这个cookie放到header里就可以了。

发送GET请求：
{% highlight java %}
URL url = new URL("URL链接");
URLConnection connection = url.openConnection();
connection.setRequestProperty("Connection", "Keep-Alive");
String returnCookie = connection.getHeaderField("Set-Cookie");
String cookie = returnCookie.substring(0, returnCookie.indexOf(";")); //取得cookie
{% endhighlight %}

发送POST请求：
{% highlight java %}
URL url = new URL("URL链接");
URLConnection connection = url.openConnection();
connection.setRequestProperty("Connection", "Keep-Alive");
connection.setRequestProperty("cookie", cookie);   //设置cookie
connection.setDoOutput(true);  //post方法必须设置
OutputStreamWriter writer = new OutputStreamWriter(connection.getOutputStream());
String queryString = "post提交的拼接字符串";
writer.write(queryString);
writer.flush();
writer.close();
{% endhighlight %}

发送请求过去之后，我们需要拿到服务器返回的数据：
{% highlight java %}
String oneLine;
String response = "";
InputStream input = connection.getInputStream();
BufferedReader reader = new BufferedReader(new InputStreamReader(input));
//将内容写入到文件
FileOutputStream out = new FileOutputStream(new File("F:/log.txt"));  
while((oneLine = reader.readLine())!=null){
    out.write((oneLine+"\r\n").getBytes());
    response += oneLine + "\r\n";
}
System.out.println(response);
{% endhighlight %}

这样我们就得到了第三方项目的数据，接下来只需要用jsoup解析数据，把我们想要的东西下来即可~~
