# Задание 5
# Эмуляция работы электронной очереди
# Напишите класс для симуляции работы электронной очереди, например, в банке.
# Система должна поддерживать добавление клиентов с указанием их приоритета (например, VIP, обычный) — 1 балл.
# Выбор клиента для следующей обработки должен учитывать приоритет — 1 балл.
# Реализуйте отчет для администрации с информацией, сколько времени заняло обслуживание клиентов — 4 балла.

import random


# Класс клиента, который может быть VIP или обычным
class Client:
    def __init__(self, is_vip):
        self.is_vip = is_vip


# Класс очереди
class Queue:
    def __init__(self, vip_time, simple_time):
        self.vip_time = vip_time
        self.simple_time = simple_time
        self.simple_queue = []
        self.vip_queue = []
        self.report_map = {
            'vip': 0,
            'simple': 0
        }

    # Добавление клиента в очередь. В зависимости от приоритета клиента добавляем в определенную очередь
    def add_client(self, client):
        if client.is_vip:
            self.vip_queue.append(client)
        else:
            self.simple_queue.append(client)

    # Удаление клиента из очереди. Сперва обрабатываем VIP очередь, затем обычную.
    def remove_client(self):
        if len(self.vip_queue) > 0:
            self.report_map['vip'] += 1
            return self.vip_queue.pop(0)
        else:
            self.report_map['simple'] += 1
            return self.simple_queue.pop(0)

    # Генерация отчета
    def generate_report(self):
        vip_qty = self.report_map['vip']
        simple_qty = self.report_map['simple']
        total_vip_time = vip_qty * self.vip_time
        total_simple_time = simple_qty * self.simple_time
        total_time = total_vip_time + total_simple_time
        print(f'Клиентов в очереди VIP: {len(self.vip_queue)}, обычных: {len(self.simple_queue)}.\n'
              f'Обработано {vip_qty} VIP клиентов, обработано {simple_qty} обычных клиентов.\n'
              f'Общее время обслуживания: {total_time}.\n'
              f'Время обслуживания VIP: {total_vip_time}, обычных: {total_simple_time}.\n'
              f'Время осблуживания оставшихся клиентов в очереди {len(self.vip_queue) * self.vip_time + len(self.simple_queue) * self.simple_time}.')


# Инициализация очереди
queue = Queue(vip_time=3, simple_time=1)

clients_qty = 10

# Добавляем клиентов в очередь
for i in range(clients_qty):
    status = random.randint(0, 1)
    client = Client(status)
    queue.add_client(client)

# Обрабатываем 4ех клиентов
for i in range(4):
    queue.remove_client()

# Генерируем отчет
queue.generate_report()
