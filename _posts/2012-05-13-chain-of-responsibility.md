---
layout: post
title: Chain of responsibility
categories: design_pattern
tags: design_pattern
---

什么情况下使用责任链模式呢？对于一个请求，有多个需要处理它的对象，并且这些处理对象之间是有顺序的，此时我们应该想到要用责任链模式(Chain of Responsbility)。
使用责任链模式有什么好处呢？它实现了请求的发起者和请求的处理者之间的解耦，并且可以有多个处理者，只要将请求交给处理的起始者，该请求就一定会被处理。

下面是一个责任链模式的例子(from 《大话设计模式》):

![UseCaseModel]({{ site.url }}/assets/img/UseCaseModel.png)

管理者抽象类：
{% highlight c# %}
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace LinkModel
{
    public abstract class Manager
    {
        protected string name;
        protected Manager superior;
        public Manager(string name)
        {
            this.name = name;
        }
        public void setSuperior(Manager superior)
        {
            this.superior = superior;
        }
        public abstract void processRequest(Request request);
    }
}
{% endhighlight %}
***
经理类：
{% highlight c# %}
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace LinkModel
{
    public class Director : Manager
    {
        public Director(string name)
            : base(name)
        { }
        public override void processRequest(Request request)
        {
            if (request.RequestType == "请假" && request.RequestNum <= 2)
            {
                Console.WriteLine("{0}:{1},{2}天被批准.by{3}.", request.RequestType, request.RequestContent, request.RequestNum, this.name);
            }
            else
            {
                if (this.superior != null)
                {
                    superior.processRequest(request);
                }
            }
        }
    }
}
{% endhighlight %}
***
总监类：
{% highlight c# %}
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace LinkModel
{
    class Inspector : Manager
    {
        public Inspector(string name) : base(name)
        {}
        public override void processRequest(Request request)
        {
            if (request.RequestType == "请假" && request.RequestNum > 2 && request.RequestNum <= 4)
            {
                Console.WriteLine("{0}:{1},{2}天被批准.by{3}.", request.RequestType, request.RequestContent, request.RequestNum, this.name);
            }
            else
            {
                if (this.superior != null)
                {
                    superior.processRequest(request);
                }
            }
        }
    }
}
{% endhighlight %}
***
总裁类：
{% highlight c# %}
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace LinkModel
{
    public class President : Manager
    {
        public President(string name) : base(name)
        {}
        public override void processRequest(Request request)
        {
            if (request.RequestType == "请假" && request.RequestNum > 4 && request.RequestNum < 7)
            {
                Console.WriteLine("{0}:{1},{2}天被批准.By{3}", request.RequestType, request.RequestContent, request.RequestNum, this.name);
            }
            else
            {
                if (superior != null)
                {
                    superior.processRequest(request);
                }
                else
                {
                    Console.WriteLine("{0}:{1},{2}天被拒绝！！By{3}.", request.RequestType, request.RequestContent, request.RequestNum, this.name);
                }
            }
        }
    }
}
{% endhighlight %}
***
请求类：
{% highlight c# %}
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace LinkModel
{
    public class Request
    {
        private string requestType;
        public string RequestType
        {
            get { return requestType; }
            set { requestType = value; }
        }
        private string requestContent;
        public string RequestContent
        {
            get { return requestContent; }
            set { requestContent = value; }
        }
        private int requestNum;
        public int RequestNum
        {
            get { return requestNum; }
            set { requestNum = value; }
        }
    }
}
{% endhighlight %}
***
客户端：
{% highlight c# %}
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace LinkModel
{
    class Program
    {
        static void Main(string[] args)
        {
            //经理
            Director jingli = new Director("经理");
            //总监
            Inspector zongjian = new Inspector("总监");
            //总裁
            President zongcai = new President("总裁");

            jingli.setSuperior(zongjian);
            zongjian.setSuperior(zongcai);

            Request req1 = new Request();
            req1.RequestType = "请假";
            req1.RequestContent = "Eric有事请假";
            req1.RequestNum = 2;
            jingli.processRequest(req1);

            Request req2 = new Request();
            req2.RequestType = "请假";
            req2.RequestContent = "Lili请假";
            req2.RequestNum = 14;
            jingli.processRequest(req2);

            Request req3 = new Request();
            req3.RequestType = "请假";
            req3.RequestContent = "Guo请假";
            req3.RequestNum = 6;
            jingli.processRequest(req3);

            Console.ReadKey();
        }
    }
}
{% endhighlight %}
***

哈哈 显示结果运行一下一目了然~~
