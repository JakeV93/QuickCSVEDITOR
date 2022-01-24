import numpy as np
import pandas as pd

records = pd.read_csv(r'C:\Users\jakev\Desktop\speakercodes.csv', index_col=False).head(5000)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 5000)
pd.set_option('display.width', None)


class SpeakerData:


    def find_duplicates(new_records):
        new_records['duplicate_tester'] = records['Last Name'] + records['First Name']
        new_records.drop_duplicates(subset=['duplicate_tester'], keep="first", inplace=True)
        del new_records['duplicate_tester']
        new_df = new_records
        new_df[new_df['speaker code'].duplicated(keep=False)]
        o = new_df.reset_index(drop=True)
        o['speaker code'] = np.where(o['speaker code'].duplicated(keep=False),
                              o['speaker code'] + o.groupby('speaker code').cumcount().add(1).astype(str),
                              o['speaker code'])

        organized_df = o.sort_index()
        print(organized_df)
        answer = input('Would you like to save to a CSV file? 1 for yes, any key for no. ')
        if answer == '1':
            organized_df.to_csv(r'C:\Users\jakev\Desktop\speaker_codes_finished.csv', index=False)
        elif answer != '1':
            print('Ok fine, I didnt want to save it anyways...')


    def create_speaker_code(self):
        del records['speaker code']
        records['speaker code'] = records['Last Name'].str[:3] + records['First Name'].str[:2]
        records["speaker code"] = records["speaker code"].str.lower()
        print(records)
        answer = input('Press 1 to save records or 2 to find and correct duplicates ')

        if answer == 1:
            records.to_csv(r'C:\Users\jakev\Desktop\speaker_codes_finished.csv', index=False)
        elif answer != 2:
            SpeakerData.find_duplicates(records)
        elif answer != 1 or 2:
            print('invalid answer')


    def start(self):
        speakerdata = SpeakerData()
        choice = input('Press 1 to auto-populate speaker codes ')
        if choice == '1':
            speakerdata.create_speaker_code()
        elif choice != '1':
            print('I literally just told you to press 1...')

speakerdata = SpeakerData()
speakerdata.start()


