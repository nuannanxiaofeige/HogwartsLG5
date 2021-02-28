# -*- coding:utf-8 -*-

from python_work.selenium_work2.page.base import Base

# 通讯录页面
_loc_add=("xpath",'//*[@class="member_colLeft_cntWrap"]/div[1]/a[1]')    #‘+’
_loc_section=("xpath","//*[@class='js_create_party']")   #‘添加部门’

#新建部门
_loc_name=("xpath",'//*[@class="member_tag_dialog_inputDlg"]/form[1]/div[1]/input[1]')  #部门名称
_loc_affiliated_section=("xpath","//*[@class='qui_btn ww_btn ww_btn_Dropdown js_toggle_party_list']/span[1]")   #所属部门
_loc_select_section=("xpath","//*[@onsubmit='return false']/div[3]/div[1]/div[1]/ul[1]/li[1]/a[1]")    #选择部门test
_loc_confirm=("xpath",'//*[@class="qui_dialog_foot ww_dialog_foot"]/a[1]')    #确定
_loc_depar=("xpath",'//*[@class="jstree jstree-1 jstree-default"]/ul[1]')   #部门列表



# 通讯录页面
class ContactPage(Base):
    # 添加部门1
    def add_department_success(self,success_name):
        self.findElement(_loc_add).click()
        self.findElement(_loc_section).click()
        self.sendKeys(_loc_name,success_name)
        self.findElement(_loc_affiliated_section).click()
        self.findElement(_loc_select_section).click()
        self.findElement(_loc_confirm).click()

    # 添加部门2（重复）
    def add_department_fail(self,fail_name):
        self.findElement(_loc_add).click()
        self.findElement(_loc_section).click()
        self.sendKeys(_loc_name,fail_name)
        self.findElement(_loc_affiliated_section).click()
        self.findElement(_loc_select_section).click()
        self.findElement(_loc_confirm).click()

    # 获取部门列表
    def get_list(self):
        eles= self.get_text(_loc_depar)
        department_list=[]
        for ele in eles:
            department_list.append(ele.text)
        print(department_list)
        return department_list

