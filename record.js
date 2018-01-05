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
            console.log("param:"+args[0]+" type:"+typeof args[0]);
          },
          onLeave: function(retval) {
            //注意:retval永远是一个对象,如果函数返回值是字符串类型,为了更好理解则要这样写
            //string_value=ObjC.classes.NSString.stringWithString_(retval)
            //console.log("Return value-> (type:"+typeof string_value+",value:"+string_value+")");
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


