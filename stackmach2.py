class StackMachine:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if not self.stack:
            raise ValueError("Стек пуст")
        return self.stack.pop()

    def execute(self, program, animals=None):
        for instruction in program:
            if isinstance(instruction, int):
                # Обработка чисел
                self.push(instruction)
            elif instruction == 'ADD':
                # Обработка оператора сложения
                right = self.pop()
                left = self.pop()
                self.push(left + right)
            elif instruction == 'SUB':
                # Обработка оператора вычитания
                right = self.pop()
                left = self.pop()
                self.push(left - right)
            elif instruction == 'MUL':
                # Обработка оператора умножения
                right = self.pop()
                left = self.pop()
                self.push(left * right)
            elif instruction == 'DIV':
                # Обработка оператора деления
                right = self.pop()
                left = self.pop()
                self.push(left // right)
            elif instruction == 'MOD':
                # Обработка оператора взятия остатка
                right = self.pop()
                left = self.pop()
                self.push(left % right)
            elif instruction == 'PRINT':
                # Обработка оператора печати
                value = self.pop()
                print(value)
            elif instruction == 'IF':
                # Обработка оператора условного ветвления
                condition = self.pop()
                if condition:
                    # Если условие истинно, выполняем следующую инструкцию
                    self.execute(program.pop(0), animals)
            elif instruction == 'WHILE':
                # Обработка оператора цикла
                expr = []
                while program[0] != 'ENDWHILE':
                    # Собираем выражение внутри цикла
                    expr.append(program.pop(0))
                # Удаляем метку 'ENDWHILE' из программы
                program.pop(0)
                while self.pop():
                    # Пока условие цикла истинно, выполняем выражение внутри цикла
                    self.execute(expr, animals)
            elif instruction == 'DO':
                # Обработка оператора цикла с постусловием
                expr = []
                while program[0] != 'ENDDO':
                    # Собираем выражение внутри цикла
                    expr.append(program.pop(0))
                # Удаляем метку 'ENDDO' из программы
                program.pop(0)
                while True:
                    # Выполняем выражение внутри цикла
                    self.execute(expr, animals)
                    # Вычисляем условие цикла
                    condition = self.pop()
                    if not condition:
                        # Если условие ложно, выходим из цикла
                        break
            elif instruction == 'FOR':
                # Обработка оператора цикла с параметром
                end = self.pop()
                start = self.pop()
                step = self.pop()
                expr = []
                while program[0] != 'ENDFOR':
                    # Собираем выражение
                    expression = []
                    while program[0] != 'DO':
                        expression.append(program.pop(0))

                    # Вычисляем выражение и получаем количество итераций
                    num_iterations = evaluate_expression(expression, stack)

                    # Удаляем DO
                    program.pop(0)

                    # Сохраняем индекс начала цикла
                    loop_start = len(program)

                    # Выполняем тело цикла num_iterations раз
                    for i in range(num_iterations):
                        # Восстанавливаем индекс начала цикла
                        program_index = loop_start

                        # Выполняем программу до ENDFOR
                        while program[0] != 'ENDFOR':
                            execute_instruction(program[0], stack)
                            program.pop(0)

                        # Удаляем ENDFOR
                        program.pop(0)

            elif instruction == 'ANIMAL':
                # Обработка оператора для работы с животными
                animal_command = self.pop()
                animal_name = self.pop()
                if animal_command == 'SAY':
                    # Обработка команды SAY - выводим имя животного
                    print(f"{animal_name} говорит: Привет!")
                elif animal_command == 'MOVE':
                    # Обработка команды MOVE - выводим информацию о передвижении животного
                    print(f"{animal_name} движется: Шаг-шаг-шаг")
                elif animal_command == 'EAT':
                    # Обработка команды EAT - выводим информацию о питании животного
                    print(f"{animal_name} ест: Жев-жев-жев")
                else:
                    raise ValueError(f"Неизвестная команда для животного: {animal_command}")
            else:
                # Если инструкция неизвестна, вызываем ошибку
                raise ValueError(f"Неизвестная инструкция: {instruction}")

# Пример использования StackMachine
if __name__ == '__main__':
    stack_machine = StackMachine()
    stack_machine.push('CAT')
    stack_machine.push('SAY')
    stack_machine.execute(['ANIMAL'])











