def minusOperation():
  TestedApps.RunAll(); #Открыть приложение
  calculator = Sys.Process("Калькулятор v7.5").WinFormsObject("Form1")
  calculator.WinFormsObject("button21").Click() #Очищаем поле вывода 
  calculator.WinFormsObject("button3").Click() #Нажать кнопку [9]
  calculator.WinFormsObject("button15").Click() #Нажать кнопку [/]
  calculator.WinFormsObject("button11").Click() #Нажать кнопку [3]
  calculator.WinFormsObject("button14").Click() #Нажать кнопку [=]
  aqObject.CheckProperty(calculator.WinFormsObject("textBox1"), 'wText', cmpEqual, "=3") #Проверка значения из поля вывода
  TestedApps.CloseAll(); #Закрыть приложение