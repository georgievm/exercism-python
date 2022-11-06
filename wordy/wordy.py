def answer(question):
    operators = {'plus': '+',
                'minus': '-',
                'multiplied by': '*',
                'divided by': '/'}
    
    # check question
    if not question.startswith('What is') or 'cubed' in question:
        raise ValueError("unknown operation")
    expr = question[:-1].replace('What is ', '')

    # replace str with operators
    for operator in list(operators.keys()):
        expr = expr.replace(operator, operators[operator])

    # check for syntax error
    splitted_expr = expr.split()
    for index, item in enumerate(splitted_expr):
        if index in [0, len(splitted_expr)-1] or index % 2 == 0:
            if item in list(operators.values()):
                raise ValueError('syntax error')
        if index % 2 != 0:
            if not item in list(operators.values()):
                raise ValueError('syntax error')
    
    result = int(splitted_expr[0])
    if len(splitted_expr) >= 3:
        for index in range(1, len(splitted_expr), 2):
            result = eval(str(result)+splitted_expr[index]+splitted_expr[index+1])
    return int(result)