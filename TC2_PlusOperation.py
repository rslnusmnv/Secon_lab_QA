def plusOperation():
  TestedApps.RunAll(); #Открыть приложение
  calculator = Sys.Process("Калькулятор v7.5").WinFormsObject("Form1") 
  calculator.WinFormsObject("button21").Click() #Очищаем поле вывода
  calculator.WinFormsObject("button9").Click() #Нажать кнопку [1]
  calculator.WinFormsObject("button4").Click() #Нажать кнопку [+]
  calculator.WinFormsObject("button11").Click() #Нажать кнопку [3]
  calculator.WinFormsObject("button14").Click() #Нажать кнопку [=]
  aqObject.CheckProperty(calculator.WinFormsObject("textBox1"), 'wText', cmpEqual, "=4") #Проверка значения из поля вывода
  TestedApps.CloseAll(); #Закрыть приложение
  