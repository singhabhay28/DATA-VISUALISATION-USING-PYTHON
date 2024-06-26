import pandas as pd
import matplotlib.pyplot as plt
while True:
    print()
    print("MAIN MENU")
    print("1. DATAFRAME STATS")
    print("2. RECORD ANALYSIS")
    print("3. DATA VISUALIZATION AS PER RECORDS")
    print("4. CUSTOMIZED DATA VISUALIZATION")
    print("5. EXIT")
    print()
    ch=int(input("ENTER YOUR CHOICE - "))
    if(ch==1):
        df=pd.read_csv("MAIN.csv")
        print()
        print("DATAFRAME PROPERTIES ")
        print("1. DISPLAY THE TRANSPOSE")
        print("2. DISPLAY COLUMN NAMES")
        print("3. DISPLAY INDEXES")
        print("4. DISPLAY THE SHAPE")
        print("5. DISPLAY THE DATA TYPES OF ALL COLUMNS")
        print("6. DISPLAY THE SIZE")
        print("7. BACK")
        print()
        ch1=int(input("ENTER YOUR CHOICE - "))
        if ch1==1:
            print()
            print(df.T)
            print()
            input("Press Enter to continue...")
            print()
        elif ch1==2:
            print()
            print(df.columns)
            print()
            input("Press Enter to continue...")
            print()
        elif ch1==3:
            print()
            print(df.index)
            print()
            input("Press Enter to continue...")
            print()
        elif ch1==4:
            print()
            print(df.shape)
            print()
            input("Press Enter to continue...")
            print()
        elif ch1==5:
            print()
            print(df.dtypes)
            print()
            input("Press Enter to continue...")
            print()
        elif ch1==6:
            print()
            print(df.size)
            print()
            input("Press Enter to continue...")
            print()
        elif ch1==7:
            pass
    elif ch==2:
            df=pd.read_csv("MAIN.csv")
            print()
            print("RECORD ANALYSIS MENU")
            print("1. HIGHEST REVIEWS (TOP 10)")
            print("2. LOWEST REVIEWS (BOTTOM 10)")
            print("3. SPECIFIC NUMBER OF RECORDS FROM TOP")
            print("4. SPECIFIC NUMBER OF RECORDS FROM BOTTOM")
            print("5. DETAIL RECORD FOR Sr.No.")
            print("6. MOST RATING (TOP 10)")
            print("7. LEAST RATING (BOTTOM 10)")
            print("8. BACK")
            print()
            ch2=int(input("ENTER YOUR CHOICE - "))
            if ch2==1:
                print()
                df1=df.loc[:,['APP NAME','CATEGORY','REVIEWS']]
                df1=df1.sort_values(by='REVIEWS',ascending=False)
                print(df1.head(10))
                print()
                input("Press Enter to continue...")
                print()
            elif ch2==2:
                print()
                df1=df.loc[:,['APP NAME','CATEGORY','REVIEWS']]
                df1=df1.sort_values(by='REVIEWS',ascending=False)
                print(df1.tail(10))
                print()
                input("Press Enter to continue...")
                print()
            elif ch2==3:
                print()
                no=int(input("HOW MANY NUMBER OF RECORDS YOU WANT TO BE PRINTED FROM THE TOP? "))
                print()
                df1=df.loc[:,['APP NAME','CATEGORY','RATING','REVIEWS','SIZE','INSTALLS']]
                print(df1.head(no))
                print()
                input("Press enter to continue...")
                print()
            elif ch2==4:
                print()
                n=int(input("HOW MANY NUMBER OF RECORDS YOU WANT TO BE PRINTED FROM THE BOTTOM? "))
                print()
                df1=df.loc[:,['APP NAME','CATEGORY','RATING','REVIEWS','SIZE','INSTALLS']]
                print(df1.tail(n))
                print()
                input("Press enter to continue...")
                print()
            elif ch2==5:
                print()
                sno=int(input("ENTER THE Sr.No. FOR WHICH YOU WANT THE DATA TO BE DISPLAYED - "))
                print()
                print(df.loc[sno])
                print()
                input('Press enter to continue...')
                print()
            elif ch2==6:
                print()
                df1=df[['APP NAME','RATING']].groupby('APP NAME').sum()
                df1=df1.sort_values(by='RATING',ascending=False)
                print(df1.head(10))
                print()
                input("Press enter to continue...")
                print()
            elif ch2==7:
                print()
                df1=df[['APP NAME','RATING']].groupby('APP NAME').sum()
                df1=df1.sort_values('RATING')
                print(df1.head(10))
                print()
                input("Press enter to continue...")
                print()
            elif ch2==8:
                pass
            else:
              print("INVALID CHOICE")
    elif(ch==3):
        df=pd.read_csv("MAIN.csv")
        print()
        print("DATA VISUALIZATION MENU - ACCORDING TO NO. OF ROWS")
        print("1. LINE PLOT")
        print("2. VERTICAL BAR PLOT")
        print("3. HORIZONTAL BAR PLOT")
        print("4. HISTOGRAM")
        print("5. EXIT THE DATA VISUALIZATION MENU")
        print()
        ch4=int(input("ENTER YOUR CHOICE - "))
        df1=pd.DataFrame()
        if ch4==1:
            print()
            n=int(input("HOW MANY RECORDS FROM THE TOP OF TABLE YOU WANT TO PLOT - "))
            df1=df.head(n)
            df1.plot(x='APP NAME',y='SIZE',kind='line',linestyle="-.",linewidth=2,color='black')
            plt.show()
        elif ch4==2:
            print()
            n=int(input("HOW MANY RECORDS FROM THE TOP OF TABLE YOU WANT TO PLOT - "))
            df1=df.head(n)
            df1.plot(x='APP NAME',y='RATING',kind="bar",color=["pink"],width=0.5)
            plt.show()
        elif ch4==3:
            print()
            n=int(input("HOW MANY RECORDS FROM THE TOP OF TABLE YOU WANT TO PLOT - "))
            df1=df.head(n)
            df1.plot(x='APP NAME',y='REVIEWS',kind="barh",color="cyan",width=0.5)
            plt.show()
        elif ch4==4:
            print()
            n=int(input("HOW MANY RECORDS FROM THE TOP OF TABLE YOU WANT TO PLOT - "))
            df1=df.head(n)
            df1.hist(color="yellow",edgecolor="pink")
            plt.show()
        elif ch4==5:
            pass
    elif(ch==4):
        df=pd.read_csv("MAIN.csv")
        print()
        print("CUSTOMIZED DATA VISUALIZATION MENU")
        print("1. BY CATEGORY")
        print("2. BY TYPE")
        print("3. BACK")
        print()
        ch5=int(input("ENTER YOUR CHOICE - "))
        df1=pd.DataFrame()
        if ch5==1:
            print()
            print("ENSURE THAT THE CATEGORY SHOULD MATCH WITH CSV RECORDS!!!")
            print()
            name=input("ENTER THE CATEGORY YOU WANT TO PLOT - ")
            print()
            print('-----OPTIONS TO PLOT----- \n1. Line Chart \n2. Bar Chart \n3. Horizontal Bar Chart \n4. Histogram \n5. Back')
            print()
            ch5_1=int(input("ENTER YOUR CHOICE - "))
            if ch5_1==1:
              df1=df.loc[df['CATEGORY']==name]
              df1=df1.loc[:,['APP NAME','RATING']]
              df1.plot(x='APP NAME',y='RATING',kind='line',linestyle="-.",linewidth=2,color='black')
              plt.show()
            elif ch5_1==2:
              df1=df.loc[df['CATEGORY']==name]
              df1=df1.loc[:,['APP NAME','RATING']]
              df1.plot(x='APP NAME',y='RATING',kind='bar',color='m')
              plt.show()
            elif ch5_1==3:
              df1=df.loc[df['CATEGORY']==name]
              df1=df1.loc[:,['APP NAME','RATING']]
              df1.plot(x='APP NAME',y='RATING',kind='barh',color='c')
              plt.show()
            elif ch5_1==4:
              df1=df.loc[df['CATEGORY']==name]
              df1=df1.loc[:,['APP NAME','RATING']]
              df1.plot(x='APP NAME',y='RATING',kind='hist',bins=15,cumulative=True)
              plt.show()
            elif cf5_1==5:
              pass
        elif ch5==2:
            print()
            print("ENSURE THAT THE TYPE(PAID OR FREE) SHOULD MATCH WITH CSV RECORDS!!!")
            print()
            types=input("ENTER THE TYPE(PAID OR FREE) YOU WANT TO PLOT - ")
            print()
            print('-----OPTIONS TO PLOT----- \n1. Line Chart \n2. Bar Chart \n3. Horizontal Bar Chart \n4. Histogram \n5. Back')
            print()
            ch5_2=int(input("ENTER YOUR CHOICE - "))
            if ch5_2==1:
              df1=df.loc[df['TYPE']==types]
              df1=df1.loc[:,['APP NAME','RATING']]
              df1.plot(x='APP NAME',y='RATING',kind='line',linestyle="-.",linewidth=2,color='black')
              plt.show()
            elif ch5_2==2:
              df1=df.loc[df['TYPE']==types]
              df1=df1.loc[:,['APP NAME','RATING']]
              df1.plot(x='APP NAME',y='RATING',kind='bar',color='m')
              plt.show()
            elif ch5_2==3:
              df1=df.loc[df['TYPE']==types]
              df1=df1.loc[:,['APP NAME','RATING']]
              df1.plot(x='APP NAME',y='RATING',kind='barh',color='c')
              plt.show()
            elif ch5_2==4:
              df1=df.loc[df['TYPE']==types]
              df1=df1.loc[:,['APP NAME','RATING']]
              df1.plot(x='APP NAME',y='RATING',kind='hist',bins=25,cumulative=True)
              plt.show()
            elif ch5_2==5:
              pass
    else:
        print()
        print("*-------------------------*INVALID CHOICE*-----------------------*")
        print("*----------------*PLEASE SELECT THE CORRECT OPTION*----------------*")
        print()
        print("      THANKS FOR VISITING, FOR MORE PROJECTS STAY TUNED WITH US        ")
