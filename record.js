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
            console.log("retval:"+retval+" type:"+typeof retval);
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

