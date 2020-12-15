def minusOperation():
  TestedApps.RunAll(); #Открыть приложение
  calculator = Sys.Process("Калькулятор v7.5").WinFormsObject("Form1")
  calculator.WinFormsObject("button21").Click() #Очищаем поле вывода 
  calculator.WinFormsObject("button2").Click() #Нажать кнопку [8]
  calculator.WinFormsObject("button13").Click() #Нажать кнопку [*]
  calculator.WinFormsObject("button5").Click() #Нажать кнопку [4]
  calculator.WinFormsObject("button14").Click() #Нажать кнопку [=]
  aqObject.CheckProperty(calculator.WinFormsObject("textBox1"), 'wText', cmpEqual, "=32") #Проверка значения из поля вывода
  TestedApps.CloseAll(); #Закрыть приложение