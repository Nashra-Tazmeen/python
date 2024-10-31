import os
import calendar
import pandas as pd 
def days_in_month(month: int, year: int) -> int:
    """Return the number of days in a given month and year."""
    if month < 1 or month > 12:
        raise ValueError("Month must be between 1 and 12.")

    return calendar.monthrange(year, month)[1] 
columns = ['Day','T','TM','Tm','SLP','H','PP','VV','V','VM','VG','RA','SN','TS','FG']  
area = {"page":1,"extraction_method":"lattice","selection_id":"F1729343946237","x1":82.50683944702148,"x2":755.0543394470214,"y1":413.2120848508155,"y2":939.4620848508155,"width":672.5475,"height":526.25,"spec_index":0}
DIR_PATH = os.path.join("new_pdfs", "Pdf_Data1")
SAVE_PATH = os.path.join("csv", "Csv_Data")

# create directory to store data
os.makedirs(SAVE_PATH, exist_ok=True)

for year in tqdm(range(2008, 2024)):
  # check if year folder exists else create one
  os.makedirs(os.path.join(SAVE_PATH, str(year)), exist_ok=True)

  for month in range(1, 13):
    try:

      pdf_path = os.path.join(DIR_PATH, str(year), str(month)+'.pdf')

      csv_path = os.path.join(SAVE_PATH, str(year), str(month)+'.csv')

      with open(pdf_path, 'rb') as file:
        df = read_pdf(file,
                      pages=1,
                      # area=area
                      )

      # get number of days in month
      DAYS_IN_MONTH = days_in_month(month, year)

      # blank dataftame
      blank_df = pd.DataFrame()

      # first dataframe
      data = df[-1].iloc[df[-1].shape[0]-2-DAYS_IN_MONTH:-2]#.to_csv(csv_path, index=False)

      for idx, col in enumerate(range(data.shape[1])):
        blank_df["columns"+str(col)] = data.iloc[:,idx].values

      blank_df.to_csv(csv_path, index=False)

      # print(type(blank_df))

      # print(f"\Extracted : {year} - {month}, Shape: {df[-2].shape}")
      # print(f"\Extracted : {year} - {month}")

    except Exception as e:
      print(f"\nConverted : {year} - {month}")
      print(f"\nError: {e}\n")