def minusOperation():
  TestedApps.RunAll(); #Открыть приложение
  calculator = Sys.Process("Калькулятор v7.5").WinFormsObject("Form1")
  calculator.WinFormsObject("button21").Click() #Очищаем поле вывода 
  calculator.WinFormsObject("button1").Click() #Нажать кнопку [7]
  calculator.WinFormsObject("button8").Click() #Нажать кнопку [-]
  calculator.WinFormsObject("button6").Click() #Нажать кнопку [5]
  calculator.WinFormsObject("button14").Click() #Нажать кнопку [=]
  aqObject.CheckProperty(calculator.WinFormsObject("textBox1"), 'wText', cmpEqual, "=2") #Проверка значения из поля вывода
  TestedApps.CloseAll(); #Закрыть приложение