import streamlit as st
from PIL import Image
from RFEM.enums import *
from RFEM.initModel import client, Model
from RFEM.Tools.GetObjectNumbersByType import GetObjectNumbersByType
from RFEM.Results.resultTables import ResultTables, GetMaxValue

st.set_page_config("Sherpa Integration", layout="wide")
st.title('Sherpa Integration')

# lst = None
# lst = client.service.get_model_list()
# st.set_page_config("Sherpa Integration", layout="wide")
# st.title('Sherpa Integration')

# col1, buff, col2 = st.columns([10,3,10])

# with col1:
#     if lst:
#         stmodel = st.selectbox('Select the Model', lst[0])

#         Model(False, stmodel)
#         #Model.clientModel.service.close_connection()
#         loadcaseList, loadcombList, loadList = [], [], []
#         loadcase = GetObjectNumbersByType(ObjectTypes.E_OBJECT_TYPE_LOAD_CASE)
#         for i in range(len(loadcase)):
#             loadcaseList.append(Model.clientModel.service.get_load_case(i+1).name)
        
#         loadcomb = GetObjectNumbersByType(ObjectTypes.E_OBJECT_TYPE_LOAD_COMBINATION)
#         for i in range(len(loadcomb)):
#             loadcombList.append(Model.clientModel.service.get_load_combination(i+1).name)
            
#         loadList.extend(loadcaseList)
#         loadList.extend(loadcombList)
        
#         nodes = GetObjectNumbersByType(ObjectTypes.E_OBJECT_TYPE_NODE)

#         with st.form("my_form"):

#             lc = st.selectbox('Select Load Case/Combination', loadList)
#             index = loadList.index(lc)+1

#             if index <= len(loadcaseList):
#                 lc = index
#                 lctype = CaseObjectType.E_OBJECT_TYPE_LOAD_CASE
#             else:
#                 lc = index - len(loadcaseList)
#                 lctype = CaseObjectType.E_OBJECT_TYPE_LOAD_COMBINATION
            
#             maxnode= len(nodes)
#             node_number = st.number_input('Node number', 1, maxnode)
            
#             submitted = st.form_submit_button("Submit")

#             forcetab = ResultTables.NodesDeformations(lctype, lc, node_number)
#             node_Vz = GetMaxValue(forcetab, 'support_forces_p_z')

#         if submitted:
#             st.subheader('Maximum shear force on node ' + str(node_number) + ' is '+ str(node_Vz) + ' kN.')

#             if node_Vz < 0:
#                 node_Vz = -1 * node_Vz

#     else:
#         st.text('There is not any open Model in RFEM.')
#         st.text('Please open at least one model in RFEM!')

# with col2:

#     if submitted:
#         check = False
#         st.text('Suitable SHERPA Connector/s:')

#         if node_Vz <= 5:
#             check = True
#             image = Image.open('img/SHERPA_XS_5.png')
#             st.image(image, width= 250)
#             st.markdown("[SHERPA XS 5](https://www.sherpa-connector.com/de/produkte/holzverbinder/sherpa-xs-m/3388_237_shop_SHERPA-XS-5.aspx?LNG=de)")

#         elif node_Vz <= 10:
#             check = True
#             image = Image.open('img/SHERPA_XS_10.png')
#             st.image(image, width= 250)
#             st.markdown("[SHERPA XS 10](https://www.sherpa-connector.com/de/produkte/holzverbinder/sherpa-xs-m/3388_238_shop_SHERPA-XS-10.aspx?LNG=de)")
        
#         elif node_Vz <= 15:
#             check = True
#             image = Image.open('img/SHERPA_XS_15.png')
#             st.image(image, width= 250)
#             st.markdown("[SHERPA XS 15](https://www.sherpa-connector.com/de/produkte/holzverbinder/sherpa-xs-m/3388_239_shop_SHERPA-XS-15.aspx?LNG=de)")

#         elif node_Vz <= 20:
#             check = True
#             image = Image.open('img/SHERPA_XS_20.png')
#             st.image(image, width= 250)
#             st.markdown("[SHERPA XS 20](https://www.sherpa-connector.com/de/produkte/holzverbinder/sherpa-xs-m/3388_240_shop_SHERPA-XS-20.aspx?LNG=de)")

#         if node_Vz <= 5:
#             check = True
#             image = Image.open('img/SHERPA_S5.png')
#             st.image(image, width= 250)
#             st.markdown("[SHERPA S5](https://www.sherpa-connector.com/de/produkte/holzverbinder/sherpa-xs-m/3388_241_shop_SHERPA-S-5.aspx?LNG=de)")

#         elif node_Vz <= 10:
#             check = True
#             image = Image.open('img/SHERPA_S10.png')
#             st.image(image, width= 250)
#             st.markdown("[SHERPA S10](https://www.sherpa-connector.com/de/produkte/holzverbinder/sherpa-xs-m/3388_242_shop_SHERPA-S-10.aspx?LNG=de)")

#         elif node_Vz <= 15:
#             check = True
#             image = Image.open('img/SHERPA_S15.png')
#             st.image(image, width= 250)
#             st.markdown("[SHERPA S15](https://www.sherpa-connector.com/de/produkte/holzverbinder/sherpa-xs-m/3388_243_shop_SHERPA-S-15.aspx?LNG=de)")

#         elif node_Vz <= 20:
#             check = True
#             image = Image.open('img/SHERPA_S20.png')
#             st.image(image, width= 250)
#             st.markdown("[SHERPA S20](https://www.sherpa-connector.com/de/produkte/holzverbinder/sherpa-xs-m/3388_244_shop_SHERPA-S-20.aspx?LNG=de)")

#         if node_Vz >= 15 and node_Vz <= 27:
#             check = True
#             image = Image.open('img/SHERPA_M15.png')
#             st.image(image, width= 250)
#             st.markdown("[SHERPA M15](https://www.sherpa-connector.com/de/produkte/holzverbinder/sherpa-xs-m/3388_245_shop_SHERPA-M-15.aspx?LNG=de)")

#         elif node_Vz >= 20 and node_Vz <= 43:
#             check = True
#             image = Image.open('img/SHERPA_M20.png')
#             st.image(image, width= 250)
#             st.markdown("[SHERPA M20](https://www.sherpa-connector.com/de/produkte/holzverbinder/sherpa-xs-m/3388_246_shop_SHERPA-M-20.aspx?LNG=de)")

#         elif node_Vz >= 25 and node_Vz <= 50:
#             check = True
#             image = Image.open('img/SHERPA_M25.png')
#             st.image(image, width= 250)
#             st.markdown("[SHERPA M25](https://www.sherpa-connector.com/de/produkte/holzverbinder/sherpa-xs-m/3388_247_shop_SHERPA-M-25.aspx?LNG=de)")

#         elif node_Vz >= 30 and node_Vz <= 58:
#             check = True
#             image = Image.open('img/SHERPA_M30.png')
#             st.image(image, width= 250)
#             st.markdown("[SHERPA M30](https://www.sherpa-connector.com/de/produkte/holzverbinder/sherpa-xs-m/3388_248_shop_SHERPA-M-30.aspx?LNG=de)")

#         elif node_Vz >= 40 and node_Vz <= 72:
#             check = True
#             image = Image.open('img/SHERPA_M40.png')
#             st.image(image, width= 250)
#             st.markdown("[SHERPA M40](https://www.sherpa-connector.com/de/produkte/holzverbinder/sherpa-xs-m/3388_249_shop_SHERPA-M-40.aspx?LNG=de)")

#         if check == False:
#             st.text('There is no suitable connector.')