# Sets the target folders and the final framework product.
# 如果工程名称和Framework的Target名称不一样的话，要自定义FMKNAME
# 例如: FMK_NAME = "MyFramework"
# FMK_NAME=${PROJECT_NAME}
# # Install dir will be the final output to the framework.
# # The following line create it in the root folder of the current project.
# INSTALL_DIR=${SRCROOT}/Products/${FMK_NAME}.framework
# # Working dir will be deleted after the framework creation.
# WRK_DIR=build
# DEVICE_DIR=${WRK_DIR}/Release-iphoneos/${FMK_NAME}.framework
# SIMULATOR_DIR=${WRK_DIR}/Release-iphonesimulator/${FMK_NAME}.framework
# # -configuration ${CONFIGURATION}
# # Clean and Building both architectures.
# xcodebuild -configuration "Release" -target "XWNewsFramework" -sdk iphoneos clean build
# xcodebuild -configuration "Release" -target "${FMK_NAME}" -sdk iphonesimulator clean build
# # Cleaning the oldest.
# if [ -d "${INSTALL_DIR}" ]
# then
# rm -rf "${INSTALL_DIR}"
# fi
# mkdir -p "${INSTALL_DIR}"
# cp -R "${DEVICE_DIR}/" "${INSTALL_DIR}/"
# cp -R "${SIMULATOR_DIR}/" "${INSTALL_DIR}/"
# # Uses the Lipo Tool to merge both binary files (i386 + armv6/armv7) into one Universal final product.
# lipo -create "${DEVICE_DIR}/${FMK_NAME}" "${SIMULATOR_DIR}/${FMK_NAME}" -output "${INSTALL_DIR}/${FMK_NAME}"
# rm -r "${WRK_DIR}"
# open "${INSTALL_DIR}"
import os
import time

# framework 的名字
FrameworkName = 'XWNewsFramework'
# 编译的路径
Build_Path = '/Users/yj/Desktop/新闻对外开放平台/XWFramework--打包和Demo/鲜闻打包工程/XWNewsFramework'

# print(Build_Path)

DEVICE_DIR='%s/build/Release-iphoneos/%s.framework'%(Build_Path,FrameworkName)

SIMULATOR_DIR='%s/build/Release-iphonesimulator/%s.framework'%(Build_Path,FrameworkName)

# os.system('cd /Users/yj/master \n')
# os.('which cd /Users/yj/master')
# mkdir/chdir/getcwd/remove/rmdir
# 编译
os.chdir('%s'%Build_Path)
os.system('xcodebuild -configuration "Release" -target %s -sdk iphoneos clean build'%(FrameworkName))
os.system('xcodebuild -configuration "Release" -target %s -sdk iphonesimulator clean build'%(FrameworkName))

time.sleep(5)

# 创建一个新闻文件夹
UniversalPath = '%s/Universal'%(Build_Path)
os.system('mkdir -p %s'%(UniversalPath))
os.system('cp -R %s/ %s/'%(DEVICE_DIR,UniversalPath))

# 合并
os.system('lipo -create %s/%s %s/%s -output %s/Universal/%s'%(DEVICE_DIR,FrameworkName,SIMULATOR_DIR,FrameworkName,Build_Path,FrameworkName))
os.system('open .')

# os.getcwd()
