### Задание 1. Ответьте письменно на вопросы:

1) Почему использование тестовых заглушек может быть полезным при написании модульных тестов?
   - Тестовые заглушки полезны при написании модульных тестов, так как они изолируют тестируемый код от внешних зависимостей, обеспечивают контроль поведения и ускоряют процесс тестирования. Они также позволяют создавать сценарии с ошибками и обеспечивают независимость тестов от внешних ресурсов
___
2) Какой тип тестовой заглушки следует использовать, если вам нужно проверить, что метод был вызван с определенными аргументами?
   - Для проверки, что метод был вызван с определенными аргументами, рекомендуется использовать spy в качестве тестовой заглушки. Шпион записывает информацию о вызовах: переданные аргументы, количество вызовов и т. д.
___
3) Какой тип тестовой заглушки следует использовать, если вам просто нужно вернуть определенное значение или исключение в ответ на вызов метода?
   - Для случаев, когда нужно просто вернуть определенное значение или сгенерировать исключение в ответ на вызов метода, нужно использовать mock.
___
4) Какой тип тестовой заглушки вы бы использовали для имитации взаимодействия с внешним API или базой данных?
   - Для имитации взаимодействия с внешним API или базой данных, нужно использовать stub. Стаб предоставляет фиксированные данные или предопределенные ответы на запросы.