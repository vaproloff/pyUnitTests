### Задание 1.

Представьте, что вы работаете над разработкой простого приложения для записной книжки, которое позволяет пользователям
добавлять, редактировать и удалять контакты.
Ваша задача - придумать как можно больше различных тестов (юнит-тесты, интеграционные тесты, сквозные тесты) для этого
приложения. Напишите название каждого теста, его тип и краткое описание того, что этот тест проверяет.
___

1. **Юнит-тест: Проверка добавления контакта**
    - Этот тест проверяет функциональность добавления нового контакта в приложение. Создается новый контакт, добавляется
      в записную книжку, а затем проверяется, что контакт успешно добавлен и содержит правильные данные.

2. **Юнит-тест: Проверка редактирования контакта**
    - Тест проверяет возможность редактирования существующего контакта. Сначала создается контакт, затем изменяются его
      данные, и в конце проверяется, что контакт отредактирован корректно.

3. **Юнит-тест: Проверка удаления контакта**
    - Этот тест проверяет функциональность удаления контакта из записной книжки. Создается контакт, затем удаляется, и в
      конце проверяется, что контакт больше не существует в записной книжке.

4. **Юнит-тест: Проверка обработки ошибок при сохранении данных**
    - Этот тест проверяет, как приложение обрабатывает ошибки при сохранении контактов. Эмулируются
      различные сценарии ошибок, такие как отсутствие доступа к базе данных, и проверяется, что приложение корректно
      обрабатывает такие ситуации.

5. **Юнит-тест: Проверка валидации контактных данных**
    - Этот тест проверяет, что приложение правильно выполняет валидацию контактных данных перед их
      добавлением. Попытка добавить контакт с некорректными данными должна привести к отклонению и несохранению
      контакта.

6. **Юнит-тест: Проверка поиска контакта по имени**
    - Тест проверяет функциональность поиска контакта по имени. Добавляются контакты с разными именами, а
      затем выполняется поиск по одному из имен. Проверяется, что поиск возвращает корректный результат.

7. **Юнит-тест: Проверка обработки дубликатов контактов**
    - Этот тест проверяет, что приложение корректно обрабатывает ситуации с дубликатами контактов.
      Добавляется контакт с уже существующим именем или номером телефона, и проверяется, что приложение предотвращает
      добавление дубликата.

8. **Интеграционный тест: Проверка сохранения данных приложения**
    - Тест проверяет, что данные контактов корректно сохраняются при выходе из приложения и повторном
      входе. Добавляются несколько контактов, приложение закрывается, затем открывается снова, и проверяется, что все
      ранее добавленные контакты присутствуют.

9. **Интеграционный тест: Проверка сортировки контактов**
    - Тест проверяет правильность сортировки контактов в записной книжке. Добавляются контакты с разными
      именами или буквенными символами, а затем проверяется, что контакты отображаются в правильном порядке.

10. **Интеграционный тест: Проверка взаимодействия с системным календарем**
    - Тест проверяет, как приложение взаимодействует с системным календарем устройства. Добавляется
      контакт с днем рождения, и затем проверяется, что этот день рождения автоматически отображается в системном
      календаре.

11. **Интеграционный тест: Проверка взаимодействия с системным временем**
    - Тест проверяет, как приложение взаимодействует с системным временем. Создается контакт с напоминанием, и
      проверяется, что приложение корректно отображает и обрабатывает это напоминание в соответствии с системным
      временем.

12. **Сквозной тест: Проверка работы интерфейса приложения**
    - Тест проверяет, как приложение ведет себя после перезапуска. Добавляются контакты, приложение закрывается, затем
      снова открывается, и проверяется, что ранее добавленные контакты сохранены и отображаются корректно.

13. **Сквозной тест: Проверка работы приложения после перезапуска**
    - Тест проверяет, как приложение ведет себя после перезапуска. Добавляются контакты, приложение закрывается, затем
      снова открывается, и проверяется, что ранее добавленные контакты сохранены и отображаются корректно.

14. **Сквозной тест: Проверка навигации по приложению**
    - Тест проверяет навигацию пользователя по всем разделам приложения. Он выполняет различные действия, такие как
      открытие меню, переключение между вкладками, и проверяет, что интерфейс отзывается корректно.

15. **Сквозной тест: Проверка ввода данных через интерфейс**
    - Тест проверяет, как приложение обрабатывает ввод данных через интерфейс. Пользователь вводит текстовую информацию,
      выбирает опции и взаимодействует с различными элементами интерфейса. Проверяется корректность отображения и
      обработки введенных данных.
