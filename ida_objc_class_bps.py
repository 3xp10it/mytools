# coding=utf8
#!/usr/bin/python
classes=ida_kernwin.ask_text(0, "", "请输入想要trace的类,以空格分开")
class_list=classes.split(" ")
for func_addr in Functions():    
    func_name=GetFunctionName(func_addr)
    for class_name in class_list:
        if class_name+" " in func_name:
            if add_bpt(func_addr):
                set_bpt_attr(func_addr,BPTATTR_FLAGS,BPT_TRACE)
                print "%s:添加断点成功" % func_name
