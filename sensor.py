from espectografo import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
import serial
import time
import numpy as np
import pandas as pd
import datetime


class MainWindow(QtWidgets.QMainWindow, Ui_Espectografo):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
       
        self.ok.clicked.connect(self.onOk)
        
   
        
    def onOk(self):
        AR1=self.AR1.value()
        AR2=self.AR2.value()
        totaltime=self.ttime.value()
        t=totaltime*(0.0028)
        if (totaltime==0):
            
            self.msg = QMessageBox()
            self.msg.setIcon(QMessageBox.Warning)
            self.msg.setText("El tiempo se muestreo debe ser mayor a 0")
            self.msg.setWindowTitle("Alerta")
            self.msg.show()
            
               
        elif(self.NING.isChecked()== True):
                       
            ser=serial.Serial()
            ser.baudrate =115200
            ser.port= '/dev/ttyUSB0'
            ser.open()
            d=np.zeros((AR1,18))
            ser.write(f"ATINTTIME={totaltime}\n".encode())
            data=ser.readline().decode().replace("OK\n","")
            ser.write(f"ATBURST={AR1},{AR2}\n".encode())
            data=ser.readline().decode().replace("OK\n","")
            print(data)
            time.sleep(1)    
            for i in range (AR1):                
                data=ser.readline().decode()
                d[i, :] = [float(elemento) for elemento in data.split(",")]
                time.sleep(t)           

            ser.close()
            df = pd.DataFrame(d, columns=["R", "S", "T", "U", "V", "W", "G", "H", "I", "J", "K", "L", "A", "B", "C", "D", "E", "F"])
            h=datetime.datetime.now()
            df.to_csv(f"/home/pi/Desktop/{h}.csv", index=False)

            self.msg = QMessageBox()
            self.msg.setIcon(QMessageBox.Information)
            self.msg.setText(f"la ubicacion del archivo es /home/pi/Desktop/{h}.csv")
            self.msg.setWindowTitle("Informacion")
            self.msg.show()
            
        elif(self.UV.isChecked()== True):
            
            ser=serial.Serial()
            ser.baudrate =115200
            ser.port= '/dev/ttyUSB0'
            ser.open()
            d=np.zeros((AR1,18))
            ser.write(f"ATINTTIME={totaltime}\n".encode())
            data=ser.readline().decode().replace("OK\n","")
            ser.write(f"ATBURST={AR1},{AR2}\n".encode())
            data=ser.readline().decode().replace("OK\n","")
            ser.write(f"ATLED1=1\n".encode())
            data=ser.readline().decode().replace("OK\n","")
            print(data)
            time.sleep(1)    
            for i in range (AR1):                
                data=ser.readline().decode()
                d[i, :] = [float(elemento) for elemento in data.split(",")]
                time.sleep(t)
                
            ser.write(f"ATLED1=0\n".encode())
            ser.close()
            
            df = pd.DataFrame(d, columns=["R", "S", "T", "U", "V", "W", "G", "H", "I", "J", "K", "L", "A", "B", "C", "D", "E", "F"])
            h=datetime.datetime.now()
            df.to_csv(f"/home/pi/Desktop/{h}.csv", index=False)
            
            self.msg = QMessageBox()
            self.msg.setIcon(QMessageBox.Information)
            self.msg.setText(f"la ubicacion del archivo es /home/pi/Desktop/{h}.csv")
            self.msg.setWindowTitle("Informacion")
            self.msg.show()
            
        elif(self.IR.isChecked()== True):
            ser=serial.Serial()
            ser.baudrate =115200
            ser.port= '/dev/ttyUSB0'
            ser.open()
            d=np.zeros((AR1,18))
            ser.write(f"ATINTTIME={totaltime}\n".encode())
            data=ser.readline().decode().replace("OK\n","")
            ser.write(f"ATBURST={AR1},{AR2}\n".encode())
            data=ser.readline().decode().replace("OK\n","")
            ser.write(f"ATLED3=1\n".encode())
            data=ser.readline().decode().replace("OK\n","")
            print(data)
            time.sleep(1)    
            for i in range (AR1):                
                data=ser.readline().decode()
                d[i, :] = [float(elemento) for elemento in data.split(",")]
                time.sleep(t)
                
            ser.write(f"ATLED3=0\n".encode())
            ser.close()
            
            df = pd.DataFrame(d, columns=["R", "S", "T", "U", "V", "W", "G", "H", "I", "J", "K", "L", "A", "B", "C", "D", "E", "F"])
            h=datetime.datetime.now()
            df.to_csv(f"/home/pi/Desktop/{h}.csv", index=False)
            
            self.msg = QMessageBox()
            self.msg.setIcon(QMessageBox.Information)
            self.msg.setText(f"la ubicacion del archivo es /home/pi/Desktop/{h}.csv")
            self.msg.setWindowTitle("Informacion")
            self.msg.show()
            
        elif(self.WHT.isChecked()== True):
            ser=serial.Serial()
            ser.baudrate =115200
            ser.port= '/dev/ttyUSB0'
            ser.open()
            d=np.zeros((AR1,18))
            ser.write(f"ATINTTIME={totaltime}\n".encode())
            data=ser.readline().decode().replace("OK\n","")
            ser.write(f"ATBURST={AR1},{AR2}\n".encode())
            data=ser.readline().decode().replace("OK\n","")
            ser.write(f"ATLED5=1\n".encode())
            data=ser.readline().decode().replace("OK\n","")
            print(data)
            time.sleep(1)    
            for i in range (AR1):                
                data=ser.readline().decode()
                d[i, :] = [float(elemento) for elemento in data.split(",")]
                time.sleep(t)
                
            ser.write(f"ATLED5=0\n".encode())
            ser.close()
            
            df = pd.DataFrame(d, columns=["R", "S", "T", "U", "V", "W", "G", "H", "I", "J", "K", "L", "A", "B", "C", "D", "E", "F"])
            h=datetime.datetime.now()
            df.to_csv(f"/home/pi/Desktop/{h}.csv", index=False)
            
            self.msg = QMessageBox()
            self.msg.setIcon(QMessageBox.Information)
            self.msg.setText(f"la ubicacion del archivo es /home/pi/Desktop/{h}.csv")
            self.msg.setWindowTitle("Informacion")
            self.msg.show()
            
        
if __name__ == "__main__":
    app=QtWidgets.QApplication([])
    window= MainWindow()
    window.show()
    app.exec_()        