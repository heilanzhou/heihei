import time
from qqyouxiang.youxiang import Base
from selenium.webdriver.common.by import By


class Bod(Base):
    qq_sum_loc = (By.XPATH, '//*[@id="switcher_plogin"]')
    qq_zh_loc = (By.XPATH, '//*[@id="u"]')
    qq_mim_loc = (By.XPATH, '//*[@id="p"]')
    qq_dl_loc = (By.ID, 'login_button')
    qq_xie_loc = (By.ID, 'composebtn')

    qq_sj_loc = (By.XPATH, '//*[@id="toAreaCtrl"]/div[2]/input')
    qq_zt_loc = (By.XPATH, '//*[@id="subject"]')
    qq_fj_loc = (By.NAME, 'UploadFile')

    qq_zw_loc = (By.XPATH, '/html/body')
    qq_fs_loc = (By.XPATH, '//*[@id="toolbar"]/div/a[1]')

    # 元素动作

    def get_sum(self):
        su = self.find_ele(Bod.qq_sum_loc)
        return su

    def get_zh(self):
        zhang = self.find_ele(Bod.qq_zh_loc)
        return zhang

    def get_mim(self):
        mi = self.find_ele(Bod.qq_mim_loc)
        return mi

    def get_dl(self):
        lu = self.find_ele(Bod.qq_dl_loc)
        return lu

    def get_xie(self):
        xi = self.find_ele(Bod.qq_xie_loc)
        return xi

    def get_sj(self):
        shou = self.find_ele(Bod.qq_sj_loc)
        return shou

    def get_zt(self):
        ti = self.find_ele(Bod.qq_zt_loc)
        return ti

    def get_fj(self):
        fu = self.find_ele(Bod.qq_fj_loc)
        return fu

    def get_zw(self):
        wen = self.find_ele(Bod.qq_zw_loc)
        return wen

    def get_fs(self):
        fa = self.find_ele(Bod.qq_fs_loc)
        return fa

    def search(self, loc):
        self.get_sum().click()
        self.get_zh().send_keys(loc)
        self.get_mim().send.keys(loc)
        self.get_dl().click()
        self.get_xie().click()

        self.get_sj().send_keys(loc)
        self.get_zt().send_keys(loc)
        self.get_fj().send_keys(loc)

        self.get_zw().send_keys(loc)
        self.get_fs().click()
        time.sleep(5)
