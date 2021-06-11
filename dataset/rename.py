import os
from argparse import ArgumentParser

contributors = {'aroni'     :1,  'nuova'    :2,   'sartaj_sis'  :3,   'fardifa' :4,  'nowshin'   :5,  'nusrat':6,
                'reshoon'   :7,  'ruhee'    :8,   'silvi'       :9,   'tahiya'  :10, 'tasfia'    :11, 'afifa':12,
                'ameera'    :13, 'ankon'    :14,  'arowa'       :15,  'bushra'  :16, 'dhru'      :17, 'eusha':18,
                'fardina'   :19, 'fariha'   :20,  'inara'       :21,  'nabila'  :22, 'nazifa'    :23, 'oishee':24,
                'sadia'     :25, 'shanila'  :26,  'shawrupa'    :27,  'rimi'    :28, 'fariha-maa':29, 'arowa_amma':30,
                'minhazjr'  :31, 'mushfiq'  :32,  'mushfiq2'    :33,  'nifty'   :34, 'sartaj'    :35, 'tiyash':36,
                'muttakin'  :37, 'afridz'   :38,  'azu'         :39,  'ishfar'  :40, 'ishrak'    :41, 'ishraq':42,
                'mahir'     :43, 'minhaz'   :44,  'mokim'       :45,  'omar'    :46, 'rajat'     :47, 'saad':48,
                'shabab'    :49, 'shoumik'  :50,  'tashu'       :51,  'wasiq'   :52, 'zunayed'   :53, 'ahsan':54,
                'farhan'    :55,  'najib'   :59,  'quib'        :57,  'sadaf'   :58, 'zico'      :59, 'fariha-bapi':60
                }
 
# Function to rename multiple files
def main(args):
  
    for count, filename in enumerate(os.listdir(args.i)):

        file_name = filename.split(".")[0]
        length = len(file_name)
        name = file_name[11: length]
        first_part = filename[0:11]

        dst = first_part + "contributor" + str(contributors[name]) + ".wav"  
        src = args.i + "/" + filename
        dst = args.i + "/" + dst
        os.rename(src, dst)
  
# Driver Code
if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument("-i", "--i", type=str, required=True, help="Input dir")

    args = parser.parse_args()

    main(args)