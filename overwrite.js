if (ObjC.available)
{
    try
    {
        var className = "PARSPedometerInfo";
        var funcName = "- integratedSteps";
        var hook = eval('ObjC.classes.' + className + '["' + funcName + '"]');
        Interceptor.attach(hook.implementation, {
          onEnter: function(args) {
            console.log("Original args0-> (type:"+typeof args[0]+",value:"+args[0]+")");
            newargs0=ptr('xxx')
            args[0]=newargs0
            console.log("New args0-> (type:"+typeof args[0]+",value:"+args[0]+")");
          },
          onLeave: function(retval) {
            //注意:retval永远是一个对象,如果函数返回值是字符串类型,为了更好理解则要这样写
            //string_value=ObjC.classes.NSString.stringWithString_(retval)
            //console.log("Original return value-> (type:"+typeof string_value+",value:"+string_value+")");
            //newretval=ObjC.classes.NSString.stringWithString_("xxxx")
            //retval.replace(newretval)
            //console.log("New return value-> (type:"+typeof newretval+",value:"+newretval+")");

            console.log("Origin return value-> (type:"+typeof retval",value:"+retval+")");
            newretval=ptr("xxxx")
            retval.replace(newretval)
            console.log("New return value-> (type:"+typeof newretval",value:"+newretval+")");
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

