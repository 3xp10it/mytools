if (ObjC.available)
{
    try
    {
        var className = "xxx";
        var funcName = "- xxx";
        var hook = eval('ObjC.classes.' + className + '["' + funcName + '"]');
        console.log("[*] Class Name: " + className);
        console.log("[*] Method Name: " + funcName);
        Interceptor.attach(hook.implementation, {
          onEnter: function(args) {
            //注意:有时args参数值在这里会是一个对象,如果函数返回值是字符串类型,为了更好理解则要这样写
            //这里假设args[2]是要记录的参数
            //ObjC.classes.NSString.stringWithString_(args[2])或者args[2].toString()或者ObjC.classes.NSString.stringWithString_(args[2]).toString()
            //具体情况需要测试下是上面这3种的哪种写法
            console.log("param:"+args[2]+" type:"+typeof args[2]);
          },
          onLeave: function(retval) {
            //注意:retval一般会返回一个对象,如果函数返回值是字符串类型,为了更好理解则要这样写
            //ObjC.classes.NSString.stringWithString_(retval)或者retval.toString()或者ObjC.classes.NSString.stringWithString_(retval).toString()
            //具体情况需要测试下是上面这3种的哪种写法
            console.log("Return value-> (type:"+typeof retval+",value:"+retval+")");
          }
        });
    }
    catch(err)
    {
        console.log("[!] Exception2: " + err.message);
    }
}
else
{
    console.log("Objective-C Runtime is not available!");
}


