from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options

from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from PyQt5 import QtCore

from PyQt5.QtCore import pyqtSignal,  QObject, QThread
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QFileDialog, QDialog, QMessageBox, QInputDialog
from PyQt5.QtWidgets import QFileDialog, QDialog, QListWidgetItem
import sys, os, shutil
from MainWindow_ui import Ui_MainWindow
import urllib.request

def connect(host='https://www.google.com'):
    try:
        urllib.request.urlopen(host, timeout=1000) #Python 3.x
        return True
    except:
        return False

def getYear (ref ) : 
    li = ref.find("(")
    hi = ref.find(")")
    if (li==hi==-1) : 
        return -1
    else : 
        try : 
            year = int(ref[li+1:hi]) 
        except ValueError : 
            year = -1 
        return year

class WorkerDoScrap(QObject) : 
    finished = pyqtSignal()
    progress = pyqtSignal(str)
    greyOut = pyqtSignal(bool)

    def __init__(self, sw, folder) : 
        super().__init__()
        self.sw = sw
        self.folder = folder

    def doScrap (self) : 
        self.greyOut.emit(True)
        if self.folder=="" : 
            return False
        try : 
            browser = self.sw.comboBox_2.currentText() 
            if browser== "Chrome" : 
                chrome_options = webdriver.ChromeOptions()
                prefs = {
                'download.default_directory': self.folder.replace("/", '\\')  ,
                "download.prompt_for_download": False,
                "download.directory_upgrade": True,
                "safebrowsing_for_trusted_sources_enabled": False,
                "safebrowsing.enabled": False
                }
                chrome_options.add_experimental_option('prefs', prefs)
                chrome_options.add_argument("--headless")
                driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options) 
                self.progress.emit("Scrapping will be done using Chrome.")
            elif browser =="Firefox" : 
                options = Options()
                options.headless = True
                options.set_preference("browser.download.folderList", 2)
                options.set_preference("browser.download.manager.showWhenStarting", False)
                options.set_preference("browser.download.dir", self.folder.replace("/", '\\'))
                options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/x-gzip")

                driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)
                self.progress.emit("Scrapping will be done using Firefox.")
        
        except : 
            self.progress.emit("There is problem with initiating the webdriver. Aborting..")
            self.greyOut.emit(False)
            self.finished.emit()
            return

        try : 
            driver.get("https://www-nds.iaea.org/exfor/ibandl.htm")
        except : 
            self.progress.emit("Problem accessing the IBANDL website. Aborting..")
            self.greyOut.emit(False)
            self.finished.emit()
            return

        driver.switch_to.frame("MenuFrame")
        targets_wd = driver.find_element(By.NAME, "selectTarget").find_elements(By.TAG_NAME, "option")
        targets = [] 
        for el in  targets_wd : targets.append(el.get_attribute("value"))
        self.progress.emit("found a list of target nuclei : "+  str(targets))
        #table = driver.find_element(By.XPATH, "//table/tbody[0]") 
        projs_wd = driver.find_elements(By.NAME, "pr")
        projs = [] 
        for t in projs_wd : projs.append(t.get_attribute("value"))
        self.progress.emit ("Found a list of projectiles : " + str(projs))
        #table = driver.find_element(By.XPATH, "//table/tbody[0]") 
        dts_wd = driver.find_elements(By.NAME, "rt")
        dts = [] 
        for t in dts_wd : dts.append(t.get_attribute("value"))
        self.progress.emit("Found a list of process types : " + str(dts))

        theta_min = self.sw.SpinBox_X_6.value()
        theta_max = self.sw.SpinBox_X_7.value()
        dataunit = str(self.sw.comboBox_3.currentText())
        processType = str(self.sw.comboBox.currentText())
        yearmin = self.sw.SpinBox_X_8.value()

        #print(theta_min, theta_max, dataunit, processType, yearmin)
        mode =10 #PIGE
        for i, m in enumerate(dts) : 
            if m==processType : 
                mode = i

        self.progress.emit("Downloading crosss section data for "+dts[mode]+", with unit type "+dataunit+"...")
        driver.switch_to.default_content()
        driver.switch_to.frame("MenuFrame")
        
        for t in targets : 
            select = Select(driver.find_element(By.NAME, "selectTarget"))
            select.select_by_value(t)
            for i, ion in enumerate(projs_wd) : 
                ibandl = driver.find_element(By.NAME, "Button1")
                ion.click() 
                dts_wd[mode].click() 
                download = ibandl.click()
                driver.switch_to.default_content()
                driver.switch_to.frame("MainFrame")
                wait = WebDriverWait(driver, 10, poll_frequency=1)
                elem = wait.until(EC.presence_of_element_located ((By.ID, "myTable")))
                #print(driver.find_element(By.ID, "myTable"))
                tables = driver.find_element(By.ID, "myTable").find_element(By.TAG_NAME, "tbody").find_elements(By.TAG_NAME, "tr") 
                if (len(tables) ==2 ) : 
                    self.progress.emit("Can not find cross section data for: "+ str(dts[mode])+ ", Target : "+ str(t)+ ", Projectile : " + str(projs[i]) )
                else : 
                    self.progress.emit("Downloading cross section data for: "+ str(dts[mode])+ ", Target : "+ str(t)+ ", Projectile : "+ str(projs[i]))
                    for i, tab in enumerate(tables) : 
                        if i>=2 : 
                            tds =  tab.find_elements(By.TAG_NAME, "td") 
                            td=  tds[2].text
                            if td=="" : 
                                #print(td)
                                continue
                            tdtheta = float(tds[2].text[:-1]) 
                            #print("Theta : ", tdtheta)
                            if not( theta_min<=tdtheta and tdtheta <= theta_max) : 
                                continue
                            els = tab.find_elements(By.CLASS_NAME, "MyButton2Link2") 
                            #print([e.text for e in els])
                            if len(els)==2 : 
                                unit = tab.find_elements(By.CLASS_NAME,"units")
                                refyear = getYear(tab.find_elements(By.CLASS_NAME, "ref")[0].text)
                                #self.progress.emit(str(refyear))
                                if refyear <= yearmin : 
                                    continue
                                assert(len(unit)!=0)
                                if dataunit=="all" : 
                                    els[1].click()
                                elif (unit[0].text == dataunit) :
                                    #self.progress.emit("clicking download button..."+dataunit)
                                    els[1].click()
                            elif len(els) ==3 : 
                                self.progress.emit("Only SigmaCal is available. Skipping the download..") 
                            else : 
                                pass

                driver.switch_to.default_content()
                driver.switch_to.frame("MenuFrame")
        self.progress.emit("Done. :-)")
        driver.quit()
        self.greyOut.emit(False)
        self.finished.emit()
        

class ScrapWindow (QtWidgets.QMainWindow, Ui_MainWindow) : 
    def __init__(self) : 
        super(ScrapWindow, self).__init__()
        self.setupUi(self)
        self.listWidget.itemDoubleClicked.connect(self.openFolder)
        self.pushButton_2.clicked.connect(self.scrap)
        self.pushButton_3.clicked.connect(self.updateSimnra)
        self.connection = False
        self.folder=""

    def openFolder (self, item) : 
        self.folder = QFileDialog.getExistingDirectory(self, 'Select a folder to save the .r33 files')
        self.listWidget.item(0).setText(self.folder)
        #print(self.folder)

    def status (self, text) : 
        self.textEdit.append(text)
        self.textEdit.repaint()
    
    def greyOutStatus(self, status) : 
        self.pushButton_2.setDisabled(status)
        self.pushButton_3.setDisabled(status)

    def scrap (self) : 
        if self.folder=="" :
            return
        #print(connect())
        self.status("Checking the connection ...")
        if connect() : 
            self.connection = True
            self.status("Connection OK") 
        else : 
            self.connection = False
            self.status("Can not connect to IBANDL website. Aborting..")
            return

        self.thread = QThread()
        self.workerScrap = WorkerDoScrap(self, self.folder) 
        self.workerScrap.moveToThread(self.thread)
        self.thread.started.connect(self.workerScrap.doScrap)

        self.workerScrap.finished.connect(self.thread.quit)
        self.workerScrap.finished.connect(self.workerScrap.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.workerScrap.progress.connect(self.status)
        self.workerScrap.greyOut.connect(self.greyOutStatus)
        #self.doScrap(self.folder)
        self.thread.start()
        

    def updateSimnra (self) : 
        self.simnraFolder = QFileDialog.getExistingDirectory(self, 'Select SIMNRA installation directory') 
        files = []
        files_simnra = []
        for (dirpath, dirnames, filenames) in os.walk(self.folder):
            files.extend(filenames)

        for (dirpath, dirnames, filenames) in os.walk(self.simnraFolder):
            files_simnra.extend(filenames)

        print(self.folder, self.simnraFolder)
        fl = []
        for f in files : 
            if not (f in files_simnra) : 
                fl.append(f)
                try : 
                    shutil.copy( self.folder+"/"+f, self.simnraFolder+"/CrSec/User/"+ f)
                except : 
                    print("Can not copy the cross section files. Aborting..")
                    return

        self.status("Copied "+ str(len(fl))+ " files from "+ str(len(files))+ " files")
        self.status("Success!")


def main():
    app = QtWidgets.QApplication(sys.argv)
    form = ScrapWindow()
    form.show()
    app.exec_()



main()

