from asyncio.windows_events import NULL
from pydoc import text
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter.filedialog import asksaveasfile
from tkinter import filedialog
from tkinter import Tk, font
from PIL import ImageTk,Image
from datetime import datetime
import tkinter
import tkinter.messagebox
import tkinter as tk
import customtkinter
import time
import sqlite3
import os
import jdatetime

root = customtkinter.CTk();
root.title("Costumers Database Manager");

width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry(f"{width/2}x{height/2}+0+0")
customtkinter.set_widget_scaling(0.55)  # widget dimensions and text size
# customtkinter.set_window_scaling(1.0)  # window geometry dimensions
root.iconbitmap("_internal/icon.ico")#_internal/
customtkinter.set_appearance_mode("dark")


global cur_scr
cur_scr = ""

#---------------------------------- Password check ----------------------------------#

def passcheck(event):
	global cur_scr
	passcheck_var = passwd.get()
	if (passcheck_var == "1362"): # Unchangeable Password based on clients request O_o
	#if (True):

		#---------------------------------- First Page ----------------------------------#

		root.unbind("<Return>")
		cur_scr="First_Page"
		passwd.delete(0, END)
		txt_label.configure(text="Please Enter your password :", text_color="white")
		welcome_frame.pack_forget();
		base_frame = customtkinter.CTkFrame(root);
		newcos_frame = customtkinter.CTkFrame(root);
		search_frame = customtkinter.CTkFrame(root);
		reports_frame = customtkinter.CTkFrame(root);
		cashplus_frame = customtkinter.CTkFrame(root);
		cashminus_frame = customtkinter.CTkFrame(root);

		base_frameL = customtkinter.CTkFrame(base_frame, corner_radius=30);
		base_frameR = customtkinter.CTkFrame(base_frame, corner_radius=30);

		base_frame.pack(expand=True, fill=BOTH);
		base_frame.grid_columnconfigure((0,1,2), weight=1);
		base_frame.grid_rowconfigure(0, weight=1);

		base_frameL.grid(row=0, column=0, sticky="NWS");
		base_frameR.grid(row=0, column=2, ipadx=20, sticky="NES");

		base_frameL.grid_columnconfigure(0,weight=1);
		base_frameL.grid_rowconfigure((0,1,2,3,4), weight=1)
		base_frameR.grid_rowconfigure(2,weight=3);
		base_frameR.grid_columnconfigure((0,1),weight=1);

		#---------------------------------- Creating a database ----------------------------------#

		# create or connect to db
		conn = sqlite3.connect("costumers.db")

		# Create cursor
		cursor = conn.cursor()

		# Create table
		cursor.execute("""CREATE TABLE IF NOT EXISTS costumers (
		    first_name text,
		    last_name text,
		    code_melli text,
		    phone text,
		    phone2 text,
		    address text,
		    cash integer
			)""")

		cursor.execute("""CREATE TABLE IF NOT EXISTS money (
			costumer_id integer ,
			cash integer,
			date text
			)""")



		cursor.execute("""SELECT *
		FROM costumers
		JOIN money ON costumers.oid = money.costumer_id""")


		# Commit changes
		conn.commit()

		# Close connection
		conn.close()

		#---------------------------------- Defining the clock ----------------------------------#

		def clock():

			# Fixing 1 hour gap
			hour = time.strftime("%H")
			hour = int(hour)
			# hour -= 1
			label_clock.configure(text=time.strftime(f"{hour}:%M:%S"))
			label_clock.after(1000,clock)

		#---------------------------------- Close Button ----------------------------------#

		def close():
			response = messagebox.askyesno("EXIT","Are you sure you want to exit the program ?");
			if response==True:
				root.destroy()
			else:
				return;
		#---------------------------------- lock Button ----------------------------------#

		def lock():
			base_frame.pack_forget();
			welcome_frame.pack(expand=True, fill=BOTH);
			root.bind("<Return>", passcheck);

		#---------------------------------- Back Button ----------------------------------#

		def backtobase(loc):
			global label_query_signl
			if (loc=="new_cos"):
				newcos_frame.pack_forget();
				base_frame.pack(expand=True, fill=BOTH);
				root.unbind("<Return>");
			if (loc=="search_sc"):
				search_frame.pack_forget()
				base_frame.pack(expand=True, fill=BOTH);
			if (loc=="reports_sc"):
				reports_frame.pack_forget()
				base_frame.pack(expand=True, fill=BOTH);
			if (loc=="cashplus_sc"):
				cashplus_frame.pack_forget()
				base_frame.pack(expand=True, fill=BOTH);
			if (loc=="cashminus_sc"):
				cashminus_frame.pack_forget()
				base_frame.pack(expand=True, fill=BOTH);

		#---------------------------------- Money Format ----------------------------------#

		def format_cash(value: int) -> str:
			raw = str(abs(value))
			return ' '.join([raw[max(i - 3, 0):i] for i in range(len(raw), 0, -3)][::-1])

		#---------------------------------- New costumer Button ----------------------------------#

		def new_cos():

			# Gird config
			global cur_scr
			cur_scr = "new_cos"

			base_frame.pack_forget();
			newcos_frame.pack(expand=True, fill=BOTH);
			
			newcos_frame.grid_columnconfigure((0,1,2), weight=1);
			newcos_frame.grid_rowconfigure(0, weight=1);

			newcos_frameL = customtkinter.CTkFrame(newcos_frame, corner_radius=30);
			newcos_frameR = customtkinter.CTkFrame(newcos_frame, corner_radius=30);

			newcos_frameL.grid(row=0, column=0, sticky="NWS");
			newcos_frameR.grid(row=0, column=2, ipadx=20, sticky="NES");

			newcos_frameR.grid_rowconfigure(2,weight=3);
			newcos_frameR.grid_columnconfigure((0,1),weight=1);

			newcos_frameL.grid_columnconfigure(0,weight=1);
			newcos_frameL.grid_rowconfigure((0,1,2,3,4,5,6,7),weight=1);

			def clock_new():
				# label_clock.configure(text=time.strftime("%X"))

				# Fixing 1 hour gap
				hour = time.strftime("%H")
				hour = int(hour)
				# hour -= 1
				label_clock_new.configure(text=time.strftime(f"{hour}:%M:%S"))
				label_clock_new.after(1000,clock_new)


			label_clock_new = customtkinter.CTkLabel(newcos_frameR, font=("Comic Sans MS",100))
			label_clock_new.grid(row=0, column=0, pady=(60,10),sticky="N", columnspan=2)
			if (weekday==5):
				label_clock2 = customtkinter.CTkLabel(newcos_frameR, text=jwn, font=("B nazanin",80, "bold"), text_color="#972727")
				label_clock2.grid(row=1, column=0, sticky="N", pady=(30,10), padx=30, columnspan=2)
			else:
				label_clock2 = customtkinter.CTkLabel(newcos_frameR, text=jwn, font=("B nazanin",80, "bold"))
				label_clock2.grid(row=1, column=0, sticky="N", pady=(30,10), padx=30, columnspan=2)
			global tnow
			tnow = jdatetime.date.today()
			label_clock3 = customtkinter.CTkLabel(newcos_frameR, text=tnow, font=("Comic Sans MS",70))
			label_clock3.grid(row=2, column=0, sticky="N", pady=30, padx=30, columnspan=2)
			button_back = customtkinter.CTkButton(newcos_frameR, text="بازگشت", width=80, corner_radius=20, font=("B nazanin", 40), command=lambda: backtobase(cur_scr))
			button_back.grid(row=3, column=1, padx=10, pady=10, ipadx=20, ipady=20, sticky="es")

			clock_new()


			def addnewcos(event):
				# Create a database or connect
				conn = sqlite3.connect("costumers.db")

				# Create cursor
				cursor = conn.cursor()

				#placing - for empty slots
				if (f_name.get()==""):
					var1="-";
				else :
					var1=f_name.get();
				if (l_name.get()==""):
					var2="-";
				else :
					var2=l_name.get();
				if (melli.get()==""):
					var3="-";
				else :
					var3=melli.get();
				if (ph_number.get()==""):
					var4="-";
				else :
					var4=ph_number.get();
				if (ph_number2.get()==""):
					var5="-";
				else :
					var5=ph_number2.get();
				if (adr.get()==""):
					var6="-";
				else :
					var6=adr.get();

				#check for first or last Name
				if (var1=="-" and var2=="-"):
					messagebox.showerror("Error","نام و یا نام خانوادگی حداقل یکی باید وارد بشه")

				else:
					# Insert into table
					cursor.execute("INSERT INTO costumers VALUES (:f_name, :l_name, :melli, :ph_number, :ph_number2, :adr, :mon)",
							{
								"f_name": var1,
								"l_name": var2,
								"melli": var3,
								"ph_number": var4,
								"ph_number2": var5,
								"adr": var6,
								"mon": 0,
							})

					messagebox.showinfo("Add Record","رکورد اضافه شد")

					# Clear the text boxes
					f_name.delete(0, END);
					l_name.delete(0, END);
					melli.delete(0, END);
					ph_number.delete(0, END);
					ph_number2.delete(0, END);
					adr.delete(0, END);
				# Commit changes
				conn.commit()

				# Close connection
				conn.close()


			# Main

			label_newcos = customtkinter.CTkLabel(newcos_frameL, corner_radius=10, text="اضافه کردن رکورد", font=("B nazanin", 70, "bold"))
			label_newcos.grid(row=0, column=0, columnspan=2, padx=30, pady=(20,10))
			f_name = customtkinter.CTkEntry(newcos_frameL, corner_radius=10, width=100, font=("B nazanin", 40, "bold"))			
			f_name.grid(row=1, column=1, padx=30, pady=10, ipadx=70)
			l_name = customtkinter.CTkEntry(newcos_frameL, corner_radius=10, width=100, font=("B nazanin", 40, "bold"))
			l_name.grid(row=2, column=1, padx=30, pady=10, ipadx=70)
			melli = customtkinter.CTkEntry(newcos_frameL, corner_radius=10, width=100, font=("B nazanin", 40, "bold"))
			melli.grid(row=3, column=1, padx=30, pady=10, ipadx=70)
			ph_number = customtkinter.CTkEntry(newcos_frameL, corner_radius=10, width=100, font=("B nazanin", 40, "bold"))
			ph_number.grid(row=4, column=1, padx=30, pady=10, ipadx=70)
			ph_number2 = customtkinter.CTkEntry(newcos_frameL, corner_radius=10, width=100, font=("B nazanin", 40, "bold"))
			ph_number2.grid(row=5, column=1, padx=30, pady=10, ipadx=70)
			adr = customtkinter.CTkEntry(newcos_frameL, corner_radius=10, width=100, font=("B nazanin", 40, "bold"))
			adr.grid(row=6, column=1, padx=30, pady=10, ipadx=70)

			label_f_name = customtkinter.CTkLabel(newcos_frameL, text="نام : ", font=("B nazanin", 50))
			label_f_name.grid(row=1, column=0, padx=30, pady=10)
			label_l_name = customtkinter.CTkLabel(newcos_frameL, text="نام خانوادگی : ", font=("B nazanin", 50))
			label_l_name.grid(row=2, column=0, padx=30, pady=10)
			label_melli = customtkinter.CTkLabel(newcos_frameL, text="کد ملی : ", font=("B nazanin", 50))
			label_melli.grid(row=3, column=0, padx=30, pady=10)
			label_ph_number = customtkinter.CTkLabel(newcos_frameL, text="شماره تماس : ", font=("B nazanin", 50))
			label_ph_number.grid(row=4, column=0, padx=30, pady=10)
			label_ph_number2 = customtkinter.CTkLabel(newcos_frameL, text="شماره تماس 2 : ", font=("B nazanin", 50))
			label_ph_number2.grid(row=5, column=0, padx=30, pady=10)
			label_adr = customtkinter.CTkLabel(newcos_frameL, text="آدرس : ", font=("B nazanin", 50))
			label_adr.grid(row=6, column=0, padx=30, pady=10)

			button_addnewcos = customtkinter.CTkButton(newcos_frameL, corner_radius=20, text="اضافه کردن", font=("B nazanin", 50, "bold"),command=lambda: addnewcos(event))
			button_addnewcos.grid(row=7, column=0, columnspan=2, padx=30, pady=20, ipadx=70, ipady=35)

			root.bind("<Return>", addnewcos);

		#---------------------------------- Search Button ----------------------------------#

		def search():

			global cur_scr, selected_choice_search

			# create or connect to db
			conn = sqlite3.connect("costumers.db")
			# Create cursor
			cursor = conn.cursor()

			cur_scr = "search_sc"
			base_frame.pack_forget();


			selected_choice_search="نام خانوادگی";

			def optionmenu_callback(choice):
				global selected_choice_search
				selected_choice_search = choice

			def query():

				global selected_choice_search

				# Deleting the results

				for label in search_frameM.grid_slaves():
					if int(label.grid_info()["row"]) != 0:
						label.grid_forget()

				cos_count.grid_forget();

				# create or connect to db
				conn = sqlite3.connect("costumers.db")
				# Create cursor
				cursor = conn.cursor()

				if (selected_choice_search=="نمایش همه"):
					cursor.execute("""SELECT first_name, last_name, code_melli, phone, phone2, address, cash, oid
					 FROM costumers
					 ORDER BY oid DESC
					 LIMIT 50""")
					records = cursor.fetchall()
					searchby.delete(0, END)

				if (selected_choice_search=="نام"):
					cursor.execute("""SELECT first_name, last_name, code_melli, phone, phone2, address, cash, oid
					 FROM costumers
					 WHERE first_name LIKE ?
					ORDER BY oid DESC
					 LIMIT 50""" , ('%' + searchby.get() + '%',))
					records = cursor.fetchall()

				if (selected_choice_search=="نام خانوادگی"):
					cursor.execute("""SELECT first_name, last_name, code_melli, phone, phone2, address, cash, oid
					 FROM costumers
					 WHERE last_name LIKE ? 
					 ORDER BY oid DESC
					 LIMIT 50""" , ( '%' + searchby.get() + '%',))
					records = cursor.fetchall()

				if (selected_choice_search=="کد ملی"):
					cursor.execute("""SELECT first_name, last_name, code_melli, phone, phone2, address, cash, oid
					 FROM costumers
					 WHERE code_melli = ?
					 ORDER BY oid DESC
					 LIMIT 50""" , (searchby.get(),))
					records = cursor.fetchall()

				if (selected_choice_search=="هرچی"):
					cursor.execute("""SELECT first_name, last_name, code_melli, phone, phone2, address, cash, oid
					 FROM costumers
					 WHERE oid = ? OR first_name = ? OR last_name = ? OR code_melli = ? OR phone = ? OR phone2 = ? OR address = ?
					 ORDER BY oid DESC
					 LIMIT 50""" , ((searchby.get()), (searchby.get()), (searchby.get()), (searchby.get()), (searchby.get()), (searchby.get()), (searchby.get())))
					records = cursor.fetchall()

				if (selected_choice_search=="بدهی"):
					cursor.execute("""SELECT first_name, last_name, code_melli, phone, phone2, address, cash, oid
					 FROM costumers
					 ORDER BY cash DESC
					 LIMIT 100""")
					records = cursor.fetchall()


				#Loop through resaults
				print_records = "";

				for i in range(8):
					RowCounter = 1
					for rec in records:
						rec_value = rec[i]  # Cache rec[i] for reuse
						print_records = str(rec_value)

						if i == 7:
							# Only need to access rec[i] once here
							cos_id = int(rec_value)
							button_change = customtkinter.CTkButton(search_frameM, text="", image=bg_image, fg_color="transparent", corner_radius=20, command=lambda v=cos_id: openrec(v))
							button_change.grid(row=RowCounter, column=0)
							RowCounter += 1
						elif i == 6:
							# Use a single method for formatting the number
							cash_posorneg = int(print_records)
							spaced_content = format_cash(cash_posorneg)  # Using the format_cash function to format the number

							if cash_posorneg > 0:
								label_query = customtkinter.CTkLabel(search_frameM, text=spaced_content, font=("B nazanin", 50, "bold"), text_color="#972727")
							elif cash_posorneg < 0:
								# Handle negative numbers by removing the minus sign
								label_query = customtkinter.CTkLabel(search_frameM, text=spaced_content.replace("-", ""), font=("B nazanin", 50, "bold"), text_color="#79B791")
							else:
								label_query = customtkinter.CTkLabel(search_frameM, text=spaced_content, font=("B nazanin", 50, "bold"))

							label_query.grid(row=RowCounter, column=i+1, padx=20, pady=15)
							RowCounter += 1
						else:
							label_query = customtkinter.CTkLabel(search_frameM, text=print_records, font=("B nazanin", 40, "bold"))
							label_query.grid(row=RowCounter, column=i+1, padx=20, pady=15)
							RowCounter += 1



				cursor.execute("SELECT * FROM costumers")
				record_counter = cursor.fetchall()

				cos_coutner = 0
				for case in record_counter:
					cos_coutner+=1;

				cos_count.configure(text=cos_coutner)
				cos_count.grid(row=0, column=0, sticky="e",padx=(20,10))
					
				# Commit changes
				conn.commit()
				# Close connection
				conn.close()

			def openrec(recID):

				toplevel = customtkinter.CTkToplevel(root);
				toplevel.title("Edit Record");
				
				toplevel.transient(root);
				toplevel.focus_force();
				editrec_frame = customtkinter.CTkFrame(toplevel);
				editrec_frame.pack(expand=True, fill=BOTH);

				editrec_frame.grid_columnconfigure((0,1), weight=1);
				editrec_frame.grid_rowconfigure((0,1,2,3,4,5,6,7), weight=1);


				def editrec(event):

					# create or connect to db
					conn = sqlite3.connect("costumers.db")
					# Create cursor
					cursor = conn.cursor()

					#placing - for empty slots
					if (f_name_editor.get()==""):
						var1="-";
					else :
						var1=f_name_editor.get();
					if (l_name_editor.get()==""):
						var2="-";
					else :
						var2=l_name_editor.get();
					if (melli_editor.get()==""):
						var3="-";
					else :
						var3=melli_editor.get();
					if (ph_number_editor.get()==""):
						var4="-";
					else :
						var4=ph_number_editor.get();
					if (ph_number2_editor.get()==""):
						var5="-";
					else :
						var5=ph_number2_editor.get();
					if (adr_editor.get()==""):
						var6="-";
					else :
						var6=adr_editor.get();

					#check for first or last Name
					if (var1=="-" and var2=="-"):
						messagebox.showerror("Error","نام و یا نام خانوادگی حداقل یکی باید وارد بشه")

					else:
						cursor.execute("""UPDATE costumers SET
						first_name = :first,
						last_name = :last,
						code_melli = :code,
						phone = :ph,
						phone2 = :ph2,
						address = :adr
						WHERE oid = :oid""",
						{'first':var1,
						'last':var2,
						'code':var3,
						'ph':var4,
						'ph2':var5,
						'adr':var6,
						'oid': recID
						})
						messagebox.showinfo("Edit Record", "رکورد با موفقیت تغییر کرد");
						f_name_editor.delete(0, END)
						l_name_editor.delete(0, END)
						melli_editor.delete(0, END)
						ph_number_editor.delete(0, END)
						ph_number2_editor.delete(0, END)
						adr_editor.delete(0, END)
						toplevel.destroy();
					

					# Commit changes
					conn.commit()
					# Close connection
					conn.close()

				def deleterec():

					# create or connect to db
					conn = sqlite3.connect("costumers.db")
					# Create cursor
					cursor = conn.cursor()

					response = messagebox.askyesno("DELETE", "مطمئنی میخوای حذفش کنی؟");
					if response==True:
						cursor.execute("DELETE from costumers WHERE oid = " + str(recID))
						cursor.execute("DELETE from money WHERE costumer_id = " + str(recID))
						
						f_name_editor.delete(0, END)
						l_name_editor.delete(0, END)
						melli_editor.delete(0, END)
						ph_number_editor.delete(0, END)
						ph_number2_editor.delete(0, END)
						adr_editor.delete(0, END)
						messagebox.showinfo("Delete Record", "مشتری حذف شد");
						toplevel.destroy();

					# Commit changes
					conn.commit()
					# Close connection
					conn.close()


				f_name_editor = customtkinter.CTkEntry(editrec_frame, width=250, height=60, corner_radius=15, font=("B nazanin", 30))
				f_name_editor.grid(row=0, column=1, padx=(0,15), pady=(30,10))
				l_name_editor = customtkinter.CTkEntry(editrec_frame, width=250, height=60, corner_radius=15, font=("B nazanin", 30))
				l_name_editor.grid(row=1, column=1, padx=(0,15), pady=10)
				melli_editor = customtkinter.CTkEntry(editrec_frame, width=250, height=60, corner_radius=15, font=("B nazanin", 30))
				melli_editor.grid(row=2, column=1, padx=(0,15), pady=10)
				ph_number_editor = customtkinter.CTkEntry(editrec_frame, width=250, height=60, corner_radius=15, font=("B nazanin", 30))
				ph_number_editor.grid(row=3, column=1, padx=(0,15), pady=10)
				ph_number2_editor = customtkinter.CTkEntry(editrec_frame, width=250, height=60, corner_radius=15, font=("B nazanin", 30))
				ph_number2_editor.grid(row=4, column=1, padx=(0,15), pady=10)
				adr_editor = customtkinter.CTkEntry(editrec_frame, width=250, height=60, corner_radius=15, font=("B nazanin", 30))
				adr_editor.grid(row=5, column=1, padx=(0,15), pady=10)

				label_f_name = customtkinter.CTkLabel(editrec_frame, text="نام : ", font=("B nazanin", 40, "bold"))
				label_f_name.grid(row=0, column=0, padx=(15,0), pady=(30,10))
				label_l_name = customtkinter.CTkLabel(editrec_frame, text="نام خانوادگی : ", font=("B nazanin", 40, "bold"))
				label_l_name.grid(row=1, column=0, padx=(15,0), pady=10)
				label_melli = customtkinter.CTkLabel(editrec_frame, text="کد ملی : ", font=("B nazanin", 40, "bold"))
				label_melli.grid(row=2, column=0, padx=(15,0), pady=10)
				label_ph_number = customtkinter.CTkLabel(editrec_frame, text="شماره تماس : ", font=("B nazanin", 40, "bold"))
				label_ph_number.grid(row=3, column=0, padx=(15,0), pady=10)
				label_ph_number2 = customtkinter.CTkLabel(editrec_frame, text="شماره تماس 2 : ", font=("B nazanin", 40, "bold"))
				label_ph_number2.grid(row=4, column=0, padx=(15,0), pady=10)
				label_adr = customtkinter.CTkLabel(editrec_frame, text="آدرس : ", font=("B nazanin", 40, "bold"))
				label_adr.grid(row=5, column=0, padx=(15,0), pady=10)

				button_edit = customtkinter.CTkButton(editrec_frame, text="ویرایش", font=("B nazanin", 40, "bold"), corner_radius=15, command=lambda : editrec(event))
				button_edit.grid(row=6, column=0, ipadx=30, ipady=10, padx=30, pady=10, columnspan=2)
				button_delete = customtkinter.CTkButton(editrec_frame, text="حذف مشتری", font=("B nazanin", 20), fg_color="#ef3a25", hover_color="#781D13",corner_radius=15, command=deleterec)
				button_delete.grid(row=7, column=0, padx=30, pady=(20,10), columnspan=2)


				# create or connect to db
				conn = sqlite3.connect("costumers.db")
				# Create cursor
				cursor = conn.cursor()

				cursor.execute("SELECT * FROM costumers WHERE oid = " + str(recID))
				record = cursor.fetchone();
				f_name_editor.insert(0, record[0])
				l_name_editor.insert(0, record[1])
				melli_editor.insert(0, record[2])
				ph_number_editor.insert(0, record[3])
				ph_number2_editor.insert(0, record[4])
				adr_editor.insert(0, record[5])


				# Commit changes
				conn.commit()
				# Close connection
				conn.close()

				toplevel.bind("<Return>", editrec);


			# Main

			def clock_search():

				# Fixing 1 hour gap
				hour = time.strftime("%H")
				hour = int(hour)
				# hour -= 1
				label_clock_search.configure(text=time.strftime(f"{hour}:%M:%S"))
				label_clock_search.after(1000,clock_search)

			search_frame.pack(expand=True, fill=BOTH);
			search_frame.grid_columnconfigure(0, weight=1);
			search_frame.grid_rowconfigure((0,1), weight=1);
			search_frame.grid_rowconfigure(2, weight=10);


			top_frame = customtkinter.CTkFrame(search_frame, corner_radius=30);
			top_frame.grid(row=0, column=0, pady=(10,0), sticky="NEWS");

			sec_frame = customtkinter.CTkFrame(search_frame, corner_radius=30);
			sec_frame.grid(row=1, column=0, ipady=5, pady=(5,0), sticky="NEWS");

			top_frame.grid_columnconfigure((0,1,2,3), weight=1);
			top_frame.grid_rowconfigure(0, weight=1);

			sec_frame.grid_columnconfigure((0,1,2,3,4,5,6,7), weight=1);
			sec_frame.grid_rowconfigure(0, weight=1);
			
			search_frameM = customtkinter.CTkScrollableFrame(search_frame, corner_radius=30);
			search_frameM.grid(row=2, column=0, pady=(5,10), sticky="NEWS");


			search_frameM.grid_rowconfigure(0, weight=1)
			search_frameM.grid_columnconfigure(0, weight=1)
			search_frameM.grid_columnconfigure((0,1,2,3,4,5,6,7,8), weight=1);
			search_frameM.grid_columnconfigure(7, weight=4);

			query_sign=["ویرایش",
			"نام",
			"نام خانوادگی",
			"کد ملی",
			"شماره تماس",
			"شماره تماس 2",
			"آدرس",
			"پول"]

			counter = 0;
			for sign in query_sign:
				label_query_sign = customtkinter.CTkLabel(search_frameM, text=query_sign[counter], font=("B nazanin", 50, "bold"))
				label_query_sign.grid(row=0, column=counter, pady=(0,20))
				counter+=1


			# showing the recent records

			cursor.execute("""SELECT first_name, last_name, code_melli, phone, phone2, address, cash, oid
			 FROM costumers
			 ORDER BY oid DESC
			 LIMIT 50""")
			records = cursor.fetchall()

			cursor.execute("SELECT * FROM costumers")
			record_counter = cursor.fetchall()

			cos_coutner = 0
			for case in record_counter:
				cos_coutner+=1;

			bg_image = customtkinter.CTkImage(dark_image=Image.open("_internal/change.png"),size=(50, 50))

			#Loop through resaults
			print_records = "";

			for i in range(8):
				RowCounter = 1
				for rec in records:
					# Cache rec[i] as it is used multiple times
					rec_value = rec[i]

					if i == 7:
						cos_id = int(rec_value)
						button_change = customtkinter.CTkButton(search_frameM, text="", image=bg_image, fg_color="transparent", corner_radius=20, command=lambda v=cos_id: openrec(v))
						button_change.grid(row=RowCounter, column=0)
						RowCounter += 1
					elif i == 6:
						# Directly convert to string once
						print_records = str(rec_value)
						cash_posorneg = int(print_records)

						# Use the format_cash function to avoid redundant code
						spaced_content = format_cash(cash_posorneg)

						if cash_posorneg > 0:
							label_query = customtkinter.CTkLabel(search_frameM, text=spaced_content, font=("B nazanin", 50, "bold"), text_color="#972727")
						elif cash_posorneg < 0:
							label_query = customtkinter.CTkLabel(search_frameM, text=spaced_content, font=("B nazanin", 50, "bold"), text_color="#79B791")
						else:
							label_query = customtkinter.CTkLabel(search_frameM, text=spaced_content, font=("B nazanin", 50, "bold"))

						label_query.grid(row=RowCounter, column=i+1, padx=20, pady=15)
						RowCounter += 1
					else:
						# Cache rec_value to avoid multiple conversions
						print_records = str(rec_value)
						label_query = customtkinter.CTkLabel(search_frameM, text=print_records, font=("B nazanin", 40, "bold"))
						label_query.grid(row=RowCounter, column=i+1, padx=20, pady=15)
						RowCounter += 1



			button_back_search = customtkinter.CTkButton(top_frame, text="بازگشت", width=80, corner_radius=20, font=("B nazanin", 40), command=lambda:backtobase(cur_scr))
			button_back_search.grid(row=0, column=3, ipady=3, ipadx=30, padx=(0,20),sticky="e")
			label_clock_search = customtkinter.CTkLabel(top_frame, font=("Comic Sans MS",80))
			label_clock_search.grid(row=0, column=2, sticky="W")
			if (weekday==5):
				label_clock2_search = customtkinter.CTkLabel(top_frame, text=jwn, font=("B nazanin",80, "bold"), text_color="#972727")
				label_clock2_search.grid(row=0, column=1, sticky="W")
			else:
				label_clock2_search = customtkinter.CTkLabel(top_frame, text=jwn, font=("B nazanin",80, "bold"))
				label_clock2_search.grid(row=0, column=1, sticky="W")
			label_clock3_search = customtkinter.CTkLabel(top_frame, text=tnow, font=("Comic Sans MS",80))
			label_clock3_search.grid(row=0, column=0, padx=(20,0), sticky="W")
			clock_search()




			label_searchby = customtkinter.CTkLabel(sec_frame, text="جستجو بر اساس", font=("B nazanin", 50, "bold"))
			label_searchby.grid(row=0, column=7, sticky="e",padx=(0,20))
			optionmenu_var = customtkinter.StringVar(value="نام خانوادگی")
			optionmenu = customtkinter.CTkOptionMenu(sec_frame, width=300, height=45, anchor=CENTER, corner_radius=15, variable =optionmenu_var, values=["نمایش همه", "نام", "نام خانوادگی", "کد ملی", "هرچی", "بدهی"], font=("B nazanin", 40, "bold"), dropdown_font=("B nazanin", 40, "bold"), command=optionmenu_callback)
			optionmenu.grid(row=0, column=6, sticky="e")
			searchby = customtkinter.CTkEntry(sec_frame, width=400, corner_radius=15, justify=CENTER, placeholder_text="جستجو", font=("B nazanin", 35, "bold"))
			searchby.grid(row=0, column=5, sticky="e")
			button_search = customtkinter.CTkButton(sec_frame,  corner_radius=15, text="نمایش", font=("B nazanin", 40,"bold"), command=query)
			button_search.grid(row=0, column=4, ipadx=20, sticky="e")
			label_cos_count = customtkinter.CTkLabel(sec_frame, text=": تعداد مشتری", font=("B nazanin", 50, "bold"))
			label_cos_count.grid(row=0, column=1, sticky="w")
			cos_count = customtkinter.CTkLabel(sec_frame, text=cos_coutner, font=("B nazanin", 50, "bold"))
			cos_count.grid(row=0, column=0, sticky="e",padx=(20,10))


			# Commit changes
			conn.commit()
			# Close connection
			conn.close()

		#---------------------------------- Reports Button ----------------------------------#

		def reports():

			global cur_scr, selected_choice_search

			# create or connect to db
			conn = sqlite3.connect("costumers.db")
			# Create cursor
			cursor = conn.cursor()

			cur_scr = "reports_sc"
			base_frame.pack_forget();

			selected_choice_search="نام خانوادگی";

			def optionmenu_callback(choice):
				global selected_choice_search
				selected_choice_search = choice


			def query():

				global selected_choice_search

				# create or connect to db
				conn = sqlite3.connect("costumers.db")
				# Create cursor
				cursor = conn.cursor()

				for label in reports_frameM.grid_slaves():
					if int(label.grid_info()["row"]) != 0:
						label.grid_forget()

				if (selected_choice_search=="نمایش همه"):
					cursor.execute("""SELECT first_name, last_name, code_melli, phone, phone2, address, cash, oid
					 FROM costumers""")
					records = cursor.fetchall()

				if (selected_choice_search=="نام"):
					cursor.execute("""SELECT first_name, last_name, code_melli, phone, phone2, address, cash, oid
					 FROM costumers
					 WHERE first_name LIKE ?""" , ('%' + searchby.get() + '%',))
					records = cursor.fetchall()

				if (selected_choice_search=="نام خانوادگی"):
					cursor.execute("""SELECT first_name, last_name, code_melli, phone, phone2, address, cash, oid
					 FROM costumers
					 WHERE last_name LIKE ? """ , ('%' + searchby.get() + '%',))
					records = cursor.fetchall()
					records.reverse()

				if (selected_choice_search=="کد ملی"):
					cursor.execute("""SELECT first_name, last_name, code_melli, phone, phone2, address, cash, oid
					 FROM costumers
					 WHERE code_melli = ? """ , (searchby.get(),))
					records = cursor.fetchall()
					records.reverse()

				if (selected_choice_search=="هرچی"):
					cursor.execute("""SELECT first_name, last_name, code_melli, phone, phone2, address, cash, oid
					 FROM costumers
					 WHERE oid = ? OR first_name = ? OR last_name = ? OR code_melli = ? OR phone = ? OR phone2 = ? OR address = ?""" , ((searchby.get()), (searchby.get()), (searchby.get()), (searchby.get()), (searchby.get()), (searchby.get()), (searchby.get())))
					records = cursor.fetchall()
					records.reverse()




				if (selected_choice_search=="نمایش همه" or (searchby.get()=="")):
					cursor.execute("""SELECT *, oid
						FROM money
						ORDER BY oid DESC
						LIMIT 50""")
					MoneyRecords = cursor.fetchall()
					ShareRecords = []
				else:
					cursor.execute("""SELECT *, oid
							FROM money
							ORDER BY oid DESC""")
					MoneyRecords = cursor.fetchall()
					ShareRecords = []



				for trans in MoneyRecords:
					for rec in records:
						if (trans[0]==rec[7]):
							ShareRecords.append((trans[0],trans[3],rec[0],rec[1],rec[2],rec[3],rec[4],trans[2],trans[1]))
				

				#loop through resaults				
				print_records = ""
				for i in range(8):
					rowcounter = 1
					for recs in ShareRecords:
						if i == 0:
							cosID_transID = [int(recs[0]), int(recs[1])]
							button_change = customtkinter.CTkButton(
								reports_frameM,
								text="",
								image=bg_image,
								fg_color="transparent",
								corner_radius=20,
								command=lambda v=cosID_transID: openrec(v)
							)
							button_change.grid(row=rowcounter, column=0)

						elif i == 1:
							amount = int(recs[8])
							spaced_content = format_cash(amount).replace("-", "") if amount < 0 else format_cash(amount)

							label_kwargs = {
								"text": spaced_content,
								"font": ("B nazanin", 50, "bold")
							}

							if amount > 0:
								label_kwargs["text_color"] = "#972727"
							elif amount < 0:
								label_kwargs["text_color"] = "#79B791"

							label_query = customtkinter.CTkLabel(reports_frameM, **label_kwargs)
							label_query.grid(row=rowcounter, column=i+6, padx=20, pady=15)

						else:
							text = str(recs[i])
							label_query = customtkinter.CTkLabel(
								reports_frameM,
								text=text,
								font=("B nazanin", 40, "bold")
							)
							label_query.grid(row=rowcounter, column=i-1, padx=20, pady=15)

						rowcounter += 1


				# Commit changes
				conn.commit()
				# Close connection
				conn.close()



			def openrec(IDs):

				toplevel = customtkinter.CTkToplevel(root);
				toplevel.title("Edit Record");
				
				# create or connect to db
				conn = sqlite3.connect("costumers.db")
				# Create cursor
				cursor = conn.cursor()

				toplevel.transient(root);
				toplevel.focus_force();
				editrec_frame = customtkinter.CTkFrame(toplevel);
				editrec_frame.pack(expand=True, fill=BOTH);

				editrec_frame.grid_columnconfigure((0,1), weight=1);
				editrec_frame.grid_rowconfigure((0,1,2,3,4,5,6,7), weight=1);

				def insert_spaces(event):
					# Get the current content of the entry widget
					content = amount.get()

					# Remove any existing spaces from the content
					content = content.replace(' ', '')

					# Insert spaces after every 3 characters (adjust as needed) starting from the right
					spaced_content = ' '.join([content[max(i-3, 0):i] for i in range(len(content), 0, -3)][::-1])

					# Update the content of the entry widget
					amount.delete(0, END)
					amount.insert(0, spaced_content)

				def editrec(event):

					# create or connect to db
					conn = sqlite3.connect("costumers.db")
					# Create cursor
					cursor = conn.cursor()

					moded_mon = amount.get().replace(" ","")
					if not moded_mon.isdigit():
						messagebox.showerror("Error", "مقدار وارد شده باید یک عدد مثبت باشه")
					else :
						cursor.execute("SELECT costumer_id, cash FROM money WHERE oid = ?" , (IDs[1],))
						records2 = cursor.fetchone()
						cursor.execute("SELECT cash FROM costumers WHERE oid = ?", (IDs[0],))
						records = cursor.fetchone()
						if (records2[1]>0):
							moded_mon=int(moded_mon)
							dif = records2[1] - moded_mon
							moded_mon2 = records[0]-dif
							cursor.execute("""UPDATE costumers
							SET cash = ?
							WHERE oid = ?""",(moded_mon2,records2[0]))

							cursor.execute("""UPDATE money
							SET cash = ?
							WHERE oid = ?""",(moded_mon,IDs[1]))

							messagebox.showinfo("Done", "رکورد با موفقیت تغییر کرد")
							toplevel.destroy()

						if (records2[1]<0):
							moded_mon= int(moded_mon)
							dif = records2[1] + moded_mon
							moded_mon2 = records[0]-dif

							cursor.execute("""UPDATE costumers
							SET cash = ?
							WHERE oid = ?""",(moded_mon2,records2[0]))

							cursor.execute("""UPDATE money
							SET cash = ?
							WHERE oid = ?""",(-moded_mon,IDs[1]))

							messagebox.showinfo("Done", "رکورد با موفقیت تغییر کرد")
							toplevel.destroy()
					# Commit changes
					conn.commit()
					# Close connection
					conn.close()

				def deleterec():

					# create or connect to db
					conn = sqlite3.connect("costumers.db")
					# Create cursor
					cursor = conn.cursor()

					cursor.execute("SELECT * FROM money WHERE oid = ?" , (IDs[1],))
					record = cursor.fetchmany()
					response = messagebox.askyesno("DELETE", "مطمئنی میخوای حذفش کنی؟");
					if response==True:
						cursor.execute("SELECT cash from costumers WHERE oid = ?",(IDs[0],))
						mon = cursor.fetchmany()
						mon = mon[0]
						cursor.execute("SELECT cash from money WHERE oid = ?", (IDs[1],))
						mod = cursor.fetchmany()
						mod = mod[0]
						mod_mon = int(mon)-int(mod)
						cursor.execute("""UPDATE costumers
						SET cash = ?
						where oid = ?""",(mod_mon,record[0]))
						cursor.execute("""DELETE from money
						WHERE oid = ?""",(IDs[1],))	
						messagebox.showinfo("Done","تراکنش با موفقیت حذف شد")
						toplevel.destroy()
					else:
						return
					# Commit changes
					conn.commit()
					# Close connection
					conn.close()



				cursor.execute("SELECT * FROM costumers WHERE oid = " + str(IDs[0]))
				record = cursor.fetchone();

				cursor.execute("SELECT * FROM money WHERE oid = " + str(IDs[1]))
				moneyrecord = cursor.fetchone();


				f_name_editor = customtkinter.CTkLabel(editrec_frame, text=record[0], font=("B nazanin", 30))
				f_name_editor.grid(row=0, column=1, padx=(0,40), pady=(30,10))
				l_name_editor = customtkinter.CTkLabel(editrec_frame, text=record[1], font=("B nazanin", 30))
				l_name_editor.grid(row=1, column=1, padx=(0,40), pady=10)
				melli_editor = customtkinter.CTkLabel(editrec_frame, text=record[2], font=("B nazanin", 30))
				melli_editor.grid(row=2, column=1, padx=(0,40), pady=10)
				ph_number_editor = customtkinter.CTkLabel(editrec_frame, text=record[3], font=("B nazanin", 30))
				ph_number_editor.grid(row=3, column=1, padx=(0,40), pady=10)
				ph_number2_editor = customtkinter.CTkLabel(editrec_frame, text=record[4], font=("B nazanin", 30))
				ph_number2_editor.grid(row=4, column=1, padx=(0,40), pady=10)
				adr_editor = customtkinter.CTkLabel(editrec_frame, text=record[5], font=("B nazanin", 30))
				adr_editor.grid(row=5, column=1, padx=(0,40), pady=10)
				if (moneyrecord[1]>0):
					PayOrRec = "پرداختی"
					posorneg = 1
					payorrec = customtkinter.CTkLabel(editrec_frame, text=PayOrRec, font=("B nazanin", 30, "bold"), text_color="#972727")
				else:
					PayOrRec = "دریافتی"
					posorneg = 0
					payorrec = customtkinter.CTkLabel(editrec_frame, text=PayOrRec, font=("B nazanin", 30, "bold"), text_color="#79B791")
				
				payorrec.grid(row=6, column=1, padx=(0,40), pady=10)


				label_f_name = customtkinter.CTkLabel(editrec_frame, text="نام : ", font=("B nazanin", 40, "bold"))
				label_f_name.grid(row=0, column=0, padx=(40,0), pady=(30,10))
				label_l_name = customtkinter.CTkLabel(editrec_frame, text="نام خانوادگی : ", font=("B nazanin", 40, "bold"))
				label_l_name.grid(row=1, column=0, padx=(40,0), pady=10)
				label_melli = customtkinter.CTkLabel(editrec_frame, text="کد ملی : ", font=("B nazanin", 40, "bold"))
				label_melli.grid(row=2, column=0, padx=(40,0), pady=10)
				label_ph_number = customtkinter.CTkLabel(editrec_frame, text="شماره تماس : ", font=("B nazanin", 40, "bold"))
				label_ph_number.grid(row=3, column=0, padx=(40,0), pady=10)
				label_ph_number2 = customtkinter.CTkLabel(editrec_frame, text="شماره تماس 2 : ", font=("B nazanin", 40, "bold"))
				label_ph_number2.grid(row=4, column=0, padx=(40,0), pady=10)
				label_adr = customtkinter.CTkLabel(editrec_frame, text="آدرس : ", font=("B nazanin", 40, "bold"))
				label_adr.grid(row=5, column=0, padx=(40,0), pady=10)
				label_payorrec = customtkinter.CTkLabel(editrec_frame, text="نوع :", font=("B nazanin", 40, "bold"))
				label_payorrec.grid(row=6, column=0, padx=(40,0), pady=10)

				amount = customtkinter.CTkEntry(editrec_frame, font=("B nazanin", 40), corner_radius=20, placeholder_text="مبلغ پرداختی", justify="center")
				amount.insert(0, abs(moneyrecord[1]))
				amount.grid(row=7, column=0, columnspan=2, padx=30, ipadx=50)
				amount.bind('', insert_spaces(event))
				amount.bind('<KeyRelease>', insert_spaces)

				button_edit = customtkinter.CTkButton(editrec_frame, text="ویرایش", font=("B nazanin", 40, "bold"), corner_radius=15, command=lambda : editrec(event))
				button_edit.grid(row=8, column=0, ipadx=30, ipady=10, padx=30, pady=10, columnspan=2)
				button_delete = customtkinter.CTkButton(editrec_frame, text="حذف رکورد", font=("B nazanin", 20), fg_color="#ef3a25", hover_color="#781D13",corner_radius=15, command=deleterec)
				button_delete.grid(row=9, column=0, padx=30, pady=(20,10), columnspan=2)

				# Commit changes
				conn.commit()
				# Close connection
				conn.close()
				toplevel.bind("<Return>", editrec);


			# Main

			def clock_search():

				# Fixing 1 hour gap
				hour = time.strftime("%H")
				hour = int(hour)
				# hour -= 1
				label_clock_search.configure(text=time.strftime(f"{hour}:%M:%S"))
				label_clock_search.after(1000,clock_search)

			reports_frame.pack(expand=True, fill=BOTH);
			reports_frame.grid_columnconfigure(0, weight=1);
			reports_frame.grid_rowconfigure((0,1), weight=1);
			reports_frame.grid_rowconfigure(2, weight=10);


			top_frame = customtkinter.CTkFrame(reports_frame, corner_radius=30);
			top_frame.grid(row=0, column=0, pady=(10,0), sticky="NEWS");

			sec_frame = customtkinter.CTkFrame(reports_frame, corner_radius=30);
			sec_frame.grid(row=1, column=0, ipady=5, pady=(5,0), sticky="NEWS");

			top_frame.grid_columnconfigure((0,1,2,3), weight=1);
			top_frame.grid_rowconfigure(0, weight=1);

			sec_frame.grid_columnconfigure((0,1,2,3,4,5,6,7), weight=1);
			sec_frame.grid_rowconfigure(0, weight=1);
			
			reports_frameM = customtkinter.CTkScrollableFrame(reports_frame, corner_radius=30);
			reports_frameM.grid(row=2, column=0, pady=(5,10), sticky="NEWS");


			reports_frameM.grid_rowconfigure(0, weight=1)
			reports_frameM.grid_columnconfigure(0, weight=1)
			reports_frameM.grid_columnconfigure((0,1,2,3,4,5,6,), weight=1);
			reports_frameM.grid_columnconfigure(7, weight=4);


			query_sign=["ویرایش",
			"نام",
			"نام خانوادگی",
			"کد ملی",
			"شماره تماس",
			"شماره تماس 2",
			"تاریخ",
			"پول"]
			counter = 0;
			for sign in query_sign:
				label_query_sign = customtkinter.CTkLabel(reports_frameM, text=query_sign[counter], font=("B nazanin", 50, "bold"))
				label_query_sign.grid(row=0, column=counter, pady=(0,20))
				counter+=1


			bg_image = customtkinter.CTkImage(dark_image=Image.open("_internal/change.png"),size=(50, 50))

			cursor.execute("""SELECT *, oid FROM money
			ORDER BY oid DESC
			LIMIT 50""")
			MoneyRecords = cursor.fetchall()

			#loop through resaults
		
			rowcounter = 1
			for rec in MoneyRecords:
				cursor.execute("""
					SELECT first_name, last_name, code_melli, phone, phone2
					FROM costumers
					WHERE oid = ?""", (rec[0],))
				CosRecords = cursor.fetchall()

				# Display customer info from CosRecords[0]
				for columncounter, value in enumerate(CosRecords[0], start=1):
					label = customtkinter.CTkLabel(reports_frameM, text=value, font=("B nazanin", 40, "bold"))
					label.grid(row=rowcounter, column=columncounter, padx=20, pady=15)

				rowcounter += 1


			# --- Second Part: Buttons, Cash, and Extra Info ---
			for i in range(3):
				rowcounter = 1
				for recs in MoneyRecords:
					if i == 0:
						cosID_transID = [int(recs[0]), int(recs[3])]
						button_change = customtkinter.CTkButton(
							reports_frameM,
							text="",
							image=bg_image,
							fg_color="transparent",
							corner_radius=20,
							command=lambda v=cosID_transID: openrec(v)
						)
						button_change.grid(row=rowcounter, column=0)
					elif i == 1:
						amount = int(recs[1])  # recs[1] assumed to be the cash amount
						spaced_content = format_cash(amount).replace("-", "") if amount < 0 else format_cash(amount)

						# Set text color based on value sign
						if amount > 0:
							color = "#972727"
						elif amount < 0:
							color = "#79B791"
						else:
							color = None  # Default text color

						label_kwargs = {
							"text": spaced_content,
							"font": ("B nazanin", 50, "bold")
						}
						if color:
							label_kwargs["text_color"] = color

						label = customtkinter.CTkLabel(reports_frameM, **label_kwargs)
						label.grid(row=rowcounter, column=i+6, padx=20, pady=15)
					else:  # i == 2
						other_info = str(recs[2])
						label = customtkinter.CTkLabel(reports_frameM, text=other_info, font=("B nazanin", 40, "bold"))
						label.grid(row=rowcounter, column=i+4, padx=20, pady=15)

					rowcounter += 1





			button_back_search = customtkinter.CTkButton(top_frame, text="بازگشت", width=80, corner_radius=20, font=("B nazanin", 40), command=lambda:backtobase(cur_scr))
			button_back_search.grid(row=0, column=3, ipady=3, ipadx=30, padx=(0,20),sticky="e")
			label_clock_search = customtkinter.CTkLabel(top_frame, font=("Comic Sans MS",80))
			label_clock_search.grid(row=0, column=2, sticky="W")
			if (weekday==5):
				label_clock2_search = customtkinter.CTkLabel(top_frame, text=jwn, font=("B nazanin",80, "bold"), text_color="#972727")
				label_clock2_search.grid(row=0, column=1, sticky="W")
			else:
				label_clock2_search = customtkinter.CTkLabel(top_frame, text=jwn, font=("B nazanin",80, "bold"))
				label_clock2_search.grid(row=0, column=1, sticky="W")
			label_clock3_search = customtkinter.CTkLabel(top_frame, text=tnow, font=("Comic Sans MS",80))
			label_clock3_search.grid(row=0, column=0, padx=(20,0), sticky="W")
			clock_search()




			label_searchby = customtkinter.CTkLabel(sec_frame, text="جستجو بر اساس", font=("B nazanin", 50, "bold"))
			label_searchby.grid(row=0, column=7, sticky="e",padx=(0,20))
			optionmenu_var = customtkinter.StringVar(value="نام خانوادگی")
			optionmenu = customtkinter.CTkOptionMenu(sec_frame, width=300, height=45, anchor=CENTER, corner_radius=15, variable=optionmenu_var, values=["نمایش همه", "نام", "نام خانوادگی", "کد ملی", "هرچی"], font=("B nazanin", 40, "bold"), dropdown_font=("B nazanin", 40, "bold"), command=optionmenu_callback)
			optionmenu.grid(row=0, column=6, sticky="e")
			searchby = customtkinter.CTkEntry(sec_frame, width=400, corner_radius=15, justify=CENTER, placeholder_text="جستجو", font=("B nazanin", 35, "bold"))
			searchby.grid(row=0, column=5, sticky="e")
			button_search = customtkinter.CTkButton(sec_frame,  corner_radius=15, text="نمایش", font=("B nazanin", 40,"bold"), command=query)
			button_search.grid(row=0, column=4, ipadx=20, sticky="e")

			# Commit changes
			conn.commit()
			# Close connection
			conn.close()
			
		#---------------------------------- Cash Plus Button ----------------------------------#

		def cashplus():

			global cur_scr, selected_choice_search, counter_query

			# create or connect to db
			conn = sqlite3.connect("costumers.db")
			# Create cursor
			cursor = conn.cursor()

			cur_scr = "cashplus_sc"
			base_frame.pack_forget();
			cashplus_frame.pack(expand=True, fill=BOTH);
			selected_choice_search="نام خانوادگی";
			
			def optionmenu_callback(choice):
				global selected_choice_search
				selected_choice_search = choice


			def query():

				global selected_choice_search

				# create or connect to db
				conn = sqlite3.connect("costumers.db")
				# Create cursor
				cursor = conn.cursor()

				for label in cashplus_frameM.grid_slaves():
					if int(label.grid_info()["row"]) != 0:
						label.grid_forget()

				if (selected_choice_search=="نمایش همه"):
					cursor.execute("""SELECT first_name, last_name, code_melli, phone, phone2, address, cash, oid
					 FROM costumers
					 ORDER BY oid DESC
					 LIMIT 50""")
					records = cursor.fetchall()
					searchby.delete(0, END)

				if (selected_choice_search=="نام"):
					cursor.execute("""SELECT first_name, last_name, code_melli, phone, phone2, address, cash, oid
					 FROM costumers
					 WHERE first_name LIKE ?
					 ORDER BY oid DESC
					 LIMIT 50""" , ('%' + searchby.get() + '%',))
					records = cursor.fetchall()

				if (selected_choice_search=="نام خانوادگی"):
					cursor.execute("""SELECT first_name, last_name, code_melli, phone, phone2, address, cash, oid
					 FROM costumers
					 WHERE last_name LIKE ?
					 ORDER BY oid DESC
					 LIMIT 50""", ('%' + searchby.get() + '%',))
					records = cursor.fetchall()

				if (selected_choice_search=="کد ملی"):
					cursor.execute("""SELECT first_name, last_name, code_melli, phone, phone2, address, cash, oid
					 FROM costumers
					 WHERE code_melli = ?
					 ORDER BY oid DESC
					 LIMIT 50""", (searchby.get(),))
					records = cursor.fetchall()

				if (selected_choice_search=="هرچی"):
					cursor.execute("""SELECT first_name, last_name, code_melli, phone, phone2, address, cash, oid
					 FROM costumers
					 WHERE oid = ? OR first_name = ? OR last_name = ? OR code_melli = ? OR phone = ? OR phone2 = ? OR address = ?
					 ORDER BY oid DESC
					 LIMIT 50""", ((searchby.get()), (searchby.get()), (searchby.get()), (searchby.get()), (searchby.get()), (searchby.get()), (searchby.get())))
					records = cursor.fetchall()


				#Loop through resaults
				print_records = "";
				
				for i in range(8):
					RowCounter = 1
					for rec in records:
						if i == 7:
							cos_id = int(rec[i])
							button_pay2 = customtkinter.CTkButton(
								cashplus_frameM,
								text="",
								image=bg_image,
								fg_color="transparent",
								hover_color="#972727",
								corner_radius=20,
								command=lambda v=cos_id: openrec(v)
							)
							button_pay2.grid(row=RowCounter, column=0)

						elif i == 6:
							amount = int(rec[i])
							spaced_content = format_cash(abs(amount))

							label_kwargs = {
								"text": spaced_content,
								"font": ("B nazanin", 50, "bold")
							}

							if amount > 0:
								label_kwargs["text_color"] = "#972727"
							elif amount < 0:
								label_kwargs["text_color"] = "#79B791"

							label_query = customtkinter.CTkLabel(cashplus_frameM, **label_kwargs)
							label_query.grid(row=RowCounter, column=i+1, padx=20, pady=15)

						else:
							text = str(rec[i])
							label_query = customtkinter.CTkLabel(
								cashplus_frameM,
								text=text,
								font=("B nazanin", 40, "bold")
							)
							label_query.grid(row=RowCounter, column=i+1, padx=20, pady=15)

						RowCounter += 1


				# Commit changes
				conn.commit()
				# Close connection
				conn.close()

			def openrec(recID):

				toplevel = customtkinter.CTkToplevel(root);
				toplevel.title("Pay");
				
				# create or connect to db
				conn = sqlite3.connect("costumers.db")
				# Create cursor
				cursor = conn.cursor()

				toplevel.transient(root);
				toplevel.focus_force();
				receive_frame = customtkinter.CTkFrame(toplevel);
				receive_frame.pack(expand=True, fill=BOTH);

				receive_frame.grid_columnconfigure((0,1), weight=1);
				receive_frame.grid_rowconfigure((0,1,2,3,4,5,6,7), weight=1);

				def insert_spaces(event):
				    # Get the current content of the entry widget
					content = amountpay.get()

					# Remove any existing spaces from the content
					content = content.replace(' ', '')

					# Insert spaces after every 3 characters (adjust as needed) starting from the right
					spaced_content = ' '.join([content[max(i-3, 0):i] for i in range(len(content), 0, -3)][::-1])

				    # Update the content of the entry widget
					amountpay.delete(0, tk.END)
					amountpay.insert(0, spaced_content)


				def pay(event):

					global tnow
				
					# create or connect to db
					conn = sqlite3.connect("costumers.db")
					# Create cursor
					cursor = conn.cursor()

					cursor.execute("SELECT oid FROM costumers WHERE oid = ?" , (str(recID),))
					record = cursor.fetchone()

					# Insert into table
					val_pay = amountpay.get()
					time2=time.strftime("%X")
					time2 = str(time2)
					tnow = str(tnow)
					timenow_complete = tnow + " / " + time2
					val_pay = val_pay.replace(" ","")

					if val_pay.isdigit():

						cursor.execute("INSERT INTO money VALUES (:id, :cash, :date)",
								{
									"id": record[0],
									"cash": val_pay,
									"date": timenow_complete
								})

						val_pay = int(val_pay);
						cursor.execute("SELECT cash FROM costumers WHERE oid = ?" , (str(recID),))
						cur_cash_tup = cursor.fetchone()
						cur_cash = cur_cash_tup[0]

						updated_cash = cur_cash+val_pay

						cursor.execute("""UPDATE costumers
						SET cash = ?
						WHERE oid = ?""",(updated_cash, str(recID)))

						messagebox.showinfo("Done","رکورد با موفقیت اضافه شد")

						amountpay.delete(0, END)
						toplevel.destroy();

					else:
						messagebox.showerror("Error","مبلغ وارد شده باید عدد صحیح باشه")
						amountpay.delete(0, END)

					# Commit changes
					conn.commit()
					# Close connection
					conn.close()

				cursor.execute("SELECT * FROM costumers WHERE oid = " + str(recID))
				record = cursor.fetchone();

				f_name_editor = customtkinter.CTkLabel(receive_frame, text=record[0], font=("B nazanin", 30))
				f_name_editor.grid(row=0, column=1, padx=(0,40), pady=(30,10))
				l_name_editor = customtkinter.CTkLabel(receive_frame, text=record[1], font=("B nazanin", 30))
				l_name_editor.grid(row=1, column=1, padx=(0,40), pady=10)
				melli_editor = customtkinter.CTkLabel(receive_frame, text=record[2], font=("B nazanin", 30))
				melli_editor.grid(row=2, column=1, padx=(0,40), pady=10)
				ph_number_editor = customtkinter.CTkLabel(receive_frame, text=record[3], font=("B nazanin", 30))
				ph_number_editor.grid(row=3, column=1, padx=(0,40), pady=10)
				ph_number2_editor = customtkinter.CTkLabel(receive_frame, text=record[4], font=("B nazanin", 30))
				ph_number2_editor.grid(row=4, column=1, padx=(0,40), pady=10)
				adr_editor = customtkinter.CTkLabel(receive_frame, text=record[5], font=("B nazanin", 30))
				adr_editor.grid(row=5, column=1, padx=(0,40), pady=10)

				label_f_name = customtkinter.CTkLabel(receive_frame, text="نام : ", font=("B nazanin", 40, "bold"))
				label_f_name.grid(row=0, column=0, padx=(40,0), pady=(30,10))
				label_l_name = customtkinter.CTkLabel(receive_frame, text="نام خانوادگی : ", font=("B nazanin", 40, "bold"))
				label_l_name.grid(row=1, column=0, padx=(40,0), pady=10)
				label_melli = customtkinter.CTkLabel(receive_frame, text="کد ملی : ", font=("B nazanin", 40, "bold"))
				label_melli.grid(row=2, column=0, padx=(40,0), pady=10)
				label_ph_number = customtkinter.CTkLabel(receive_frame, text="شماره تماس : ", font=("B nazanin", 40, "bold"))
				label_ph_number.grid(row=3, column=0, padx=(40,0), pady=10)
				label_ph_number2 = customtkinter.CTkLabel(receive_frame, text="شماره تماس 2 : ", font=("B nazanin", 40, "bold"))
				label_ph_number2.grid(row=4, column=0, padx=(40,0), pady=10)
				label_adr = customtkinter.CTkLabel(receive_frame, text="آدرس : ", font=("B nazanin", 40, "bold"))
				label_adr.grid(row=5, column=0, padx=(40,0), pady=10)

				amountpay = customtkinter.CTkEntry(receive_frame, font=("B nazanin", 40), corner_radius=20, placeholder_text="مبلغ پرداختی", justify="center")
				amountpay.grid(row=6, column=0, columnspan=2, padx=30, ipadx=50)
				amountpay.bind('<KeyRelease>', insert_spaces)

				button_pay = customtkinter.CTkButton(receive_frame, text="پرداخت", font=("B nazanin", 40, "bold"), corner_radius=15, command=lambda : pay(event))
				button_pay.grid(row=7, column=0, ipadx=30, ipady=8, padx=30, pady=10, columnspan=2)


				# Commit changes
				conn.commit()
				# Close connection
				conn.close()
				toplevel.bind("<Return>", pay);



			# Main

			def clock_cashplus():

				# Fixing 1 hour gap
				hour = time.strftime("%H")
				hour = int(hour)
				# hour -= 1
				label_clock_cashplus.configure(text=time.strftime(f"{hour}:%M:%S"))
				label_clock_cashplus.after(1000,clock_cashplus)

			cashplus_frame.grid_columnconfigure(0, weight=1);
			cashplus_frame.grid_rowconfigure((0,1), weight=1);
			cashplus_frame.grid_rowconfigure(2, weight=10);


			top_frame = customtkinter.CTkFrame(cashplus_frame, corner_radius=30);
			top_frame.grid(row=0, column=0, ipady=5, pady=(10,0), sticky="NEWS");

			sec_frame = customtkinter.CTkFrame(cashplus_frame, corner_radius=30);
			sec_frame.grid(row=1, column=0, ipady=5, pady=(5,0), sticky="NEWS");

			top_frame.grid_columnconfigure((0,1,2,3), weight=1);
			top_frame.grid_rowconfigure(0, weight=1);

			sec_frame.grid_columnconfigure((0,1,2,3,4,5,6,7), weight=1);
			sec_frame.grid_rowconfigure(0, weight=1);
			
			cashplus_frameM = customtkinter.CTkScrollableFrame(cashplus_frame, corner_radius=30);
			cashplus_frameM.grid(row=2, column=0, pady=(5,10), sticky="NEWS");


			cashplus_frameM.grid_rowconfigure(0, weight=1)
			cashplus_frameM.grid_columnconfigure(0, weight=1)
			cashplus_frameM.grid_columnconfigure((0,1,2,3,4,5,6,7), weight=1);
			cashplus_frameM.grid_columnconfigure(7, weight=4);

			query_sign=["پرداخت",
			"نام",
			"نام خانوادگی",
			"کد ملی",
			"شماره تماس",
			"شماره تماس 2",
			"آدرس",
			"پول"]
			counter = 0;
			for sign in query_sign:
				label_query_sign = customtkinter.CTkLabel(cashplus_frameM, text=query_sign[counter], font=("B nazanin", 50, "bold"))
				label_query_sign.grid(row=0, column=counter, pady=(0,20))
				counter+=1


			# showing the recent records

			cursor.execute("""SELECT first_name, last_name, code_melli, phone, phone2, address, cash, oid
			 FROM costumers
			 ORDER BY oid DESC
			 LIMIT 50""")
			records = cursor.fetchall()

			# bg_image = .PhotoImage(file="change.png")
			bg_image = customtkinter.CTkImage(dark_image=Image.open("_internal/red.png"),size=(80, 50))

			#Loop through resaults
			print_records = "";

			for i in range(8):
				RowCounter = 1
				for rec in records:
					if i == 7:
						cos_id = int(rec[i])
						button_pay1 = customtkinter.CTkButton(
							cashplus_frameM,
							text="",
							image=bg_image,
							fg_color="transparent",
							hover_color="#972727",
							corner_radius=20,
							command=lambda v=cos_id: openrec(v)
						)
						button_pay1.grid(row=RowCounter, column=0)

					elif i == 6:
						amount = int(rec[i])
						spaced_content = format_cash(abs(amount))

						label_kwargs = {
							"text": spaced_content,
							"font": ("B nazanin", 50, "bold")
						}

						if amount > 0:
							label_kwargs["text_color"] = "#972727"  # red
						elif amount < 0:
							label_kwargs["text_color"] = "#79B791"  # green

						label_query = customtkinter.CTkLabel(cashplus_frameM, **label_kwargs)
						label_query.grid(row=RowCounter, column=i+1, padx=20, pady=15)

					else:
						text = str(rec[i])
						label_query = customtkinter.CTkLabel(
							cashplus_frameM,
							text=text,
							font=("B nazanin", 40, "bold")
						)
						label_query.grid(row=RowCounter, column=i+1, padx=20, pady=15)

					RowCounter += 1

			button_back_cashplus = customtkinter.CTkButton(top_frame, text="بازگشت", width=80, corner_radius=20, font=("B nazanin", 40), command=lambda:backtobase(cur_scr))
			button_back_cashplus.grid(row=0, column=3, ipady=3, ipadx=30, padx=(0,20),sticky="e")
			label_clock_cashplus = customtkinter.CTkLabel(top_frame, font=("Comic Sans MS",80))
			label_clock_cashplus.grid(row=0, column=2, sticky="W")
			if (weekday==5):
				label_clock2_cashplus = customtkinter.CTkLabel(top_frame, text=jwn, font=("B nazanin",80, "bold"), text_color="#972727")
				label_clock2_cashplus.grid(row=0, column=1, sticky="W")
			else:
				label_clock2_cashplus = customtkinter.CTkLabel(top_frame, text=jwn, font=("B nazanin",80, "bold"))
				label_clock2_cashplus.grid(row=0, column=1, sticky="W")
			label_clock3_cashplus = customtkinter.CTkLabel(top_frame, text=tnow, font=("Comic Sans MS",80))
			label_clock3_cashplus.grid(row=0, column=0, padx=(20,0), sticky="W")
			clock_cashplus()


			label_searchby = customtkinter.CTkLabel(sec_frame, text="جستجو بر اساس", font=("B nazanin", 50, "bold"))
			label_searchby.grid(row=0, column=7, sticky="e",padx=(0,20))
			optionmenu_var = customtkinter.StringVar(value="نام خانوادگی")
			optionmenu = customtkinter.CTkOptionMenu(sec_frame, width=300, height=45, anchor=CENTER, corner_radius=15, variable =optionmenu_var ,values=["نمایش همه", "نام", "نام خانوادگی", "کد ملی", "هرچی"], font=("B nazanin", 40, "bold"), dropdown_font=("B nazanin", 40, "bold"), command=optionmenu_callback)
			optionmenu.grid(row=0, column=6, sticky="e")
			searchby = customtkinter.CTkEntry(sec_frame, width=400, corner_radius=15, justify=CENTER, placeholder_text="جستجو", font=("B nazanin", 35, "bold"))
			searchby.grid(row=0, column=5, sticky="e")
			button_search = customtkinter.CTkButton(sec_frame,  corner_radius=15, text="نمایش", font=("B nazanin", 40,"bold"), command=query)
			button_search.grid(row=0, column=4, ipadx=20, sticky="e")

			# Commit changes
			conn.commit()
			# Close connection
			conn.close()

		#---------------------------------- Cash Minus Button ----------------------------------#

		def cashminus():

			global cur_scr, selected_choice_search, counter_query

			# create or connect to db
			conn = sqlite3.connect("costumers.db")
			# Create cursor
			cursor = conn.cursor()

			cur_scr = "cashminus_sc"
			base_frame.pack_forget();
			cashminus_frame.pack(expand=True, fill=BOTH);
			selected_choice_search="نام خانوادگی";

			def optionmenu_callback(choice):
				global selected_choice_search
				selected_choice_search = choice


			def query():

				global selected_choice_search

				# create or connect to db
				conn = sqlite3.connect("costumers.db")
				# Create cursor
				cursor = conn.cursor()

				for label in cashminus_frameM.grid_slaves():
					if int(label.grid_info()["row"]) != 0:
						label.grid_forget()

				

				if (selected_choice_search=="نمایش همه"):
					cursor.execute("""SELECT first_name, last_name, code_melli, phone, phone2, address, cash, oid
					 FROM costumers
					 ORDER BY oid DESC
					 LIMIT 50""")
					records = cursor.fetchall()
					searchby.delete(0, END)

				if (selected_choice_search=="نام"):
					cursor.execute("""SELECT first_name, last_name, code_melli, phone, phone2, address, cash, oid
					 FROM costumers
					 WHERE first_name LIKE ?
					 ORDER BY oid DESC
					 LIMIT 50""" , ('%' + searchby.get() + '%',))
					records = cursor.fetchall()

				if (selected_choice_search=="نام خانوادگی"):
					cursor.execute("""SELECT first_name, last_name, code_melli, phone, phone2, address, cash, oid
					 FROM costumers
					 WHERE last_name LIKE ?
					 ORDER BY oid DESC
					 LIMIT 50""" , ('%' + searchby.get() + '%',))
					records = cursor.fetchall()

				if (selected_choice_search=="کد ملی"):
					cursor.execute("""SELECT first_name, last_name, code_melli, phone, phone2, address, cash, oid
					 FROM costumers
					 WHERE code_melli = ?
					 ORDER BY oid DESC
					 LIMIT 50""" , (searchby.get(),))
					records = cursor.fetchall()

				if (selected_choice_search=="هرچی"):
					cursor.execute("""SELECT first_name, last_name, code_melli, phone, phone2, address, cash, oid
					 FROM costumers
					 WHERE oid = ? OR first_name = ? OR last_name = ? OR code_melli = ? OR phone = ? OR phone2 = ? OR address = ?
					 ORDER BY oid DESC
					 LIMIT 50""" , ((searchby.get()), (searchby.get()), (searchby.get()), (searchby.get()), (searchby.get()), (searchby.get()), (searchby.get())))
					records = cursor.fetchall()



				#Loop through resaults
				print_records = "";

				for i in range(8):
					row_counter = 1
					for rec in records:
						if i == 7:
							cos_id = int(rec[i])
							button_receive2 = customtkinter.CTkButton(
								cashminus_frameM,
								text="",
								image=bg_image,
								fg_color="transparent",
								hover_color="#79B791",
								corner_radius=20,
								command=lambda v=cos_id: openrec(v)
							)
							button_receive2.grid(row=row_counter, column=0)

						elif i == 6:
							print_records = str(rec[i])
							cash_posorneg = int(print_records)
							spaced_content = ' '.join([print_records[max(j-3, 0):j] for j in range(len(print_records), 0, -3)][::-1])

							if cash_posorneg > 0:
								label_kwargs = {
									"text": spaced_content,
									"font": ("B nazanin", 50, "bold"),
									"text_color": "#972727"
								}
							elif cash_posorneg < 0:
								spaced_content = spaced_content.replace("-", "")
								label_kwargs = {
									"text": spaced_content,
									"font": ("B nazanin", 50, "bold"),
									"text_color": "#79B791"
								}
							else:
								label_kwargs = {
									"text": spaced_content,
									"font": ("B nazanin", 50, "bold")
								}

							label = customtkinter.CTkLabel(cashminus_frameM, **label_kwargs)
							label.grid(row=row_counter, column=i+1, padx=20, pady=15)

						else:
							label_kwargs = {
								"text": str(rec[i]),
								"font": ("B nazanin", 40, "bold")
							}
							label = customtkinter.CTkLabel(cashminus_frameM, **label_kwargs)
							label.grid(row=row_counter, column=i+1, padx=20, pady=15)

						row_counter += 1

				# Commit changes
				conn.commit()
				# Close connection
				conn.close()


			def openrec(recID):

				toplevel = customtkinter.CTkToplevel(root);
				toplevel.title("Receive");
				
				# create or connect to db
				conn = sqlite3.connect("costumers.db")
				# Create cursor
				cursor = conn.cursor()

				toplevel.transient(root);
				toplevel.focus_force();
				receive_frame = customtkinter.CTkFrame(toplevel);
				receive_frame.pack(expand=True, fill=BOTH);

				receive_frame.grid_columnconfigure((0,1), weight=1);
				receive_frame.grid_rowconfigure((0,1,2,3,4,5,6,7), weight=1);

				def insert_spaces(event):
				    # Get the current content of the entry widget
					content = amountreceive.get()

					# Remove any existing spaces from the content
					content = content.replace(' ', '')

				    # Insert spaces after every 3 characters (adjust as needed) starting from the right
					spaced_content = ' '.join([content[max(i-3, 0):i] for i in range(len(content), 0, -3)][::-1])

				    # Update the content of the entry widget
					amountreceive.delete(0, tk.END)
					amountreceive.insert(0, spaced_content)

				def receive(event):

					global tnow

					# create or connect to db
					conn = sqlite3.connect("costumers.db")
					# Create cursor
					cursor = conn.cursor()

					cursor.execute("SELECT oid FROM costumers WHERE oid = ?" , (str(recID),))
					record = cursor.fetchone()
						
					# Insert into table
					val_recieve = amountreceive.get()
					time2=time.strftime("%X")
					time2 = str(time2)
					tnow = str(tnow)
					timenow_complete = tnow + " / " + time2

					val_recieve = val_recieve.replace(" ","")

					if val_recieve.isdigit():

						val_recieve = "-" + val_recieve
						cursor.execute("INSERT INTO money VALUES (:id, :cash, :date)",
								{
									"id": record[0],
									"cash": val_recieve,
									"date": timenow_complete
								})

						val_recieve = int(val_recieve);
						cursor.execute("SELECT cash FROM costumers WHERE oid = ?" , (str(recID),))
						cur_cash_tup = cursor.fetchone()
						cur_cash = cur_cash_tup[0]

						updated_cash = cur_cash+val_recieve

						cursor.execute("""UPDATE costumers
						SET cash = ?
						WHERE oid = ?""",(updated_cash, (str(recID))))

						messagebox.showinfo("Done","رکورد با موفقیت اضافه شد")

						amountreceive.delete(0, END)
						toplevel.destroy()

					else:
						messagebox.showerror("Error","مبلغ وارد شده باید عدد صحیح باشه")
						amountreceive.delete(0, tk.END)

					# Commit changes
					conn.commit()
					# Close connection
					conn.close()
					#pardakhti ghermez



				cursor.execute("SELECT * FROM costumers WHERE oid = " + str(recID))
				record = cursor.fetchone();

				f_name_editor = customtkinter.CTkLabel(receive_frame, text=record[0], font=("B nazanin", 30))
				f_name_editor.grid(row=0, column=1, padx=(0,40), pady=(30,10))
				l_name_editor = customtkinter.CTkLabel(receive_frame, text=record[1], font=("B nazanin", 30))
				l_name_editor.grid(row=1, column=1, padx=(0,40), pady=10)
				melli_editor = customtkinter.CTkLabel(receive_frame, text=record[2], font=("B nazanin", 30))
				melli_editor.grid(row=2, column=1, padx=(0,40), pady=10)
				ph_number_editor = customtkinter.CTkLabel(receive_frame, text=record[3], font=("B nazanin", 30))
				ph_number_editor.grid(row=3, column=1, padx=(0,40), pady=10)
				ph_number2_editor = customtkinter.CTkLabel(receive_frame, text=record[4], font=("B nazanin", 30))
				ph_number2_editor.grid(row=4, column=1, padx=(0,40), pady=10)
				adr_editor = customtkinter.CTkLabel(receive_frame, text=record[5], font=("B nazanin", 30))
				adr_editor.grid(row=5, column=1, padx=(0,40), pady=10)

				label_f_name = customtkinter.CTkLabel(receive_frame, text="نام : ", font=("B nazanin", 40, "bold"))
				label_f_name.grid(row=0, column=0, padx=(40,0), pady=(30,10))
				label_l_name = customtkinter.CTkLabel(receive_frame, text="نام خانوادگی : ", font=("B nazanin", 40, "bold"))
				label_l_name.grid(row=1, column=0, padx=(40,0), pady=10)
				label_melli = customtkinter.CTkLabel(receive_frame, text="کد ملی : ", font=("B nazanin", 40, "bold"))
				label_melli.grid(row=2, column=0, padx=(40,0), pady=10)
				label_ph_number = customtkinter.CTkLabel(receive_frame, text="شماره تماس : ", font=("B nazanin", 40, "bold"))
				label_ph_number.grid(row=3, column=0, padx=(40,0), pady=10)
				label_ph_number2 = customtkinter.CTkLabel(receive_frame, text="شماره تماس 2 : ", font=("B nazanin", 40, "bold"))
				label_ph_number2.grid(row=4, column=0, padx=(40,0), pady=10)
				label_adr = customtkinter.CTkLabel(receive_frame, text="آدرس : ", font=("B nazanin", 40, "bold"))
				label_adr.grid(row=5, column=0, padx=(40,0), pady=10)

				amountreceive = customtkinter.CTkEntry(receive_frame, font=("B nazanin", 40), corner_radius=20, placeholder_text="مبلغ دریافتی", justify="center")
				amountreceive.grid(row=6, column=0, columnspan=2, padx=30, ipadx=50)
				amountreceive.bind('<KeyRelease>', insert_spaces)

				button_receive = customtkinter.CTkButton(receive_frame, text="دریافت", font=("B nazanin", 40, "bold"), corner_radius=15, command=lambda : receive(event))
				button_receive.grid(row=7, column=0, ipadx=30, ipady=8, padx=30, pady=10, columnspan=2)

				# Commit changes
				conn.commit()
				# Close connection
				conn.close()
				
				toplevel.bind("<Return>", receive);


			# Main

			def clock_cashminus():

				# Fixing 1 hour gap
				hour = time.strftime("%H")
				hour = int(hour)
				# hour -= 1
				label_clock_cashminus.configure(text=time.strftime(f"{hour}:%M:%S"))
				label_clock_cashminus.after(1000,clock_cashminus)

			cashminus_frame.grid_columnconfigure(0, weight=1);
			cashminus_frame.grid_rowconfigure((0,1), weight=1);
			cashminus_frame.grid_rowconfigure(2, weight=10);


			top_frame = customtkinter.CTkFrame(cashminus_frame, corner_radius=30);
			top_frame.grid(row=0, column=0, ipady=5, pady=(10,0), sticky="NEWS");

			sec_frame = customtkinter.CTkFrame(cashminus_frame, corner_radius=30);
			sec_frame.grid(row=1, column=0, ipady=5, pady=(5,0), sticky="NEWS");

			top_frame.grid_columnconfigure((0,1,2,3), weight=1);
			top_frame.grid_rowconfigure(0, weight=1);

			sec_frame.grid_columnconfigure((0,1,2,3,4,5,6,7), weight=1);
			sec_frame.grid_rowconfigure(0, weight=1);
			
			cashminus_frameM = customtkinter.CTkScrollableFrame(cashminus_frame, corner_radius=30);
			cashminus_frameM.grid(row=2, column=0, pady=(5,10), sticky="NEWS");


			cashminus_frameM.grid_rowconfigure(0, weight=1)
			cashminus_frameM.grid_columnconfigure(0, weight=1)
			cashminus_frameM.grid_columnconfigure((0,1,2,3,4,5,6,7), weight=1);
			cashminus_frameM.grid_columnconfigure(7, weight=4);

			query_sign=["دریافت",
			"نام",
			"نام خانوادگی",
			"کد ملی",
			"شماره تماس",
			"شماره تماس 2",
			"آدرس",
			"پول"]
			counter = 0;
			for sign in query_sign:
				label_query_sign = customtkinter.CTkLabel(cashminus_frameM, text=query_sign[counter], font=("B nazanin", 50, "bold"))
				label_query_sign.grid(row=0, column=counter, pady=(0,20))
				counter+=1


			# showing the recent records

			cursor.execute("""SELECT first_name, last_name, code_melli, phone, phone2, address, cash, oid
			 FROM costumers
			 ORDER BY oid DESC
			 LIMIT 50""")
			records = cursor.fetchall()

			bg_image = customtkinter.CTkImage(dark_image=Image.open("_internal/green.png"),size=(80, 50))

			#Loop through resaults
			print_records = "";

			for i in range(8):
				row_counter = 1
				for rec in records:
					if i == 7:
						cos_id = int(rec[i])
						button_receive1 = customtkinter.CTkButton(
							cashminus_frameM,
							text="",
							image=bg_image,
							fg_color="transparent",
							hover_color="#79B791",
							corner_radius=20,
							command=lambda v=cos_id: openrec(v)
						)
						button_receive1.grid(row=row_counter, column=0)

					elif i == 6:
						print_records = str(rec[i])
						cash_posorneg = int(print_records)
						spaced_content = ' '.join([print_records[max(j - 3, 0):j] for j in range(len(print_records), 0, -3)][::-1])

						if cash_posorneg > 0:
							label_kwargs = {
								"text": spaced_content,
								"font": ("B nazanin", 50, "bold"),
								"text_color": "#972727"
							}
						elif cash_posorneg < 0:
							spaced_content = spaced_content.replace("-", "")
							label_kwargs = {
								"text": spaced_content,
								"font": ("B nazanin", 50, "bold"),
								"text_color": "#79B791"
							}
						else:
							label_kwargs = {
								"text": spaced_content,
								"font": ("B nazanin", 50, "bold")
							}

						label = customtkinter.CTkLabel(cashminus_frameM, **label_kwargs)
						label.grid(row=row_counter, column=i+1, padx=20, pady=15)

					else:
						label_kwargs = {
							"text": str(rec[i]),
							"font": ("B nazanin", 40, "bold")
						}
						label = customtkinter.CTkLabel(cashminus_frameM, **label_kwargs)
						label.grid(row=row_counter, column=i+1, padx=20, pady=15)

					row_counter += 1
	

			button_back_cashminus = customtkinter.CTkButton(top_frame, text="بازگشت", width=80, corner_radius=20, font=("B nazanin", 40), command=lambda:backtobase(cur_scr))
			button_back_cashminus.grid(row=0, column=3, ipady=3, ipadx=30, padx=(0,20),sticky="e")
			label_clock_cashminus = customtkinter.CTkLabel(top_frame, font=("Comic Sans MS",80))
			label_clock_cashminus.grid(row=0, column=2, sticky="W")
			if (weekday==5):
				label_clock2_cashminus = customtkinter.CTkLabel(top_frame, text=jwn, font=("B nazanin",80, "bold"), text_color="#972727")
				label_clock2_cashminus.grid(row=0, column=1, sticky="W")
			else:
				label_clock2_cashminus = customtkinter.CTkLabel(top_frame, text=jwn, font=("B nazanin",80, "bold"))
				label_clock2_cashminus.grid(row=0, column=1, sticky="W")
			label_clock3_cashminus = customtkinter.CTkLabel(top_frame, text=tnow, font=("Comic Sans MS",80))
			label_clock3_cashminus.grid(row=0, column=0, padx=(20,0), sticky="W")
			clock_cashminus()


			label_searchby = customtkinter.CTkLabel(sec_frame, text="جستجو بر اساس", font=("B nazanin", 50, "bold"))
			label_searchby.grid(row=0, column=7, sticky="e",padx=(0,20))
			optionmenu_var = customtkinter.StringVar(value="نام خانوادگی")
			optionmenu = customtkinter.CTkOptionMenu(sec_frame, width=300, height=45, anchor=CENTER, corner_radius=15, variable=optionmenu_var, values=["نمایش همه", "نام", "نام خانوادگی", "کد ملی", "هرچی"], font=("B nazanin", 40, "bold"), dropdown_font=("B nazanin", 40, "bold"), command=optionmenu_callback)
			optionmenu.grid(row=0, column=6, sticky="e")
			searchby = customtkinter.CTkEntry(sec_frame, width=400, corner_radius=15, justify=CENTER, placeholder_text="جستجو", font=("B nazanin", 35, "bold"))
			searchby.grid(row=0, column=5, sticky="e")
			button_search = customtkinter.CTkButton(sec_frame,  corner_radius=15, text="نمایش", font=("B nazanin", 40,"bold"), command=query)
			button_search.grid(row=0, column=4, ipadx=20, sticky="e")
			# Commit changes
			conn.commit()
			# Close connection
			conn.close()

		#---------------------------------- First page left frame ----------------------------------#

		button_newCostumer = customtkinter.CTkButton(base_frameL, corner_radius=20, text="مشتری جدید", font=("B nazanin", 60, "bold"), command=new_cos)
		button_newCostumer.grid(row=0, column=0, padx=10, pady=(20, 10), ipadx=100, ipady=37, sticky="news")
		button_searchCostumer = customtkinter.CTkButton(base_frameL, corner_radius=20, text="جستجو و ویرایش", font=("B nazanin", 60, "bold"), command=search)
		button_searchCostumer.grid(row=1, column=0, padx=10, pady=10, ipadx=133, ipady=37, sticky="news")
		button_reportCostumer = customtkinter.CTkButton(base_frameL, corner_radius=20, text="گزارشات", font=("B nazanin", 60, "bold"), command=reports)
		button_reportCostumer.grid(row=2, column=0, padx=10, pady=10, ipadx=127, ipady=37, sticky="news")
		button_cashPlus = customtkinter.CTkButton(base_frameL, corner_radius=20, text="سند پرداختی", font=("B nazanin", 60, "bold"), command=cashplus)
		button_cashPlus.grid(row=3, column=0, padx=10, pady=10, ipadx=100, ipady=37, sticky="news")
		button_cashMinus = customtkinter.CTkButton(base_frameL, corner_radius=20, text="سند دریافتی", font=("B nazanin", 60, "bold"), command=cashminus)
		button_cashMinus.grid(row=4, column=0, padx=10, pady=10, ipadx=104, ipady=37, sticky="news")

		#---------------------------------- First page right frame ----------------------------------#

		weekday = time.strftime("%w")
		weekday = int(weekday)
		j_week_name = ["یک شنبه",
		"دو شنبه",
		"سه شنبه",
		"چهارشنبه",
		"پنج شنبه",
		"جمعه",
		"شنبه"]
		jwn = j_week_name[weekday]
		label_clock = customtkinter.CTkLabel(base_frameR, font=("Comic Sans MS",100))
		label_clock.grid(row=0, column=0, sticky="N", pady=(60,10), columnspan=2)
		if (weekday==5):
			label_clock2 = customtkinter.CTkLabel(base_frameR, text=jwn, font=("B nazanin",80, "bold"), text_color="#972727")
			label_clock2.grid(row=1, column=0, sticky="N", pady=(30,10), padx=30, columnspan=2)
		else:
			label_clock2 = customtkinter.CTkLabel(base_frameR, text=jwn, font=("B nazanin",80, "bold"))
			label_clock2.grid(row=1, column=0, sticky="N", pady=(30,10), padx=30, columnspan=2)
		global tnow
		tnow = jdatetime.date.today()
		label_clock3 = customtkinter.CTkLabel(base_frameR, text=tnow, font=("Comic Sans MS",70))
		label_clock3.grid(row=2, column=0, sticky="N", pady=30, padx=30, columnspan=2)
		button_lock = customtkinter.CTkButton(base_frameR, text="قفل کردن", width=80, corner_radius=20, font=("B nazanin", 40), command=lock)
		button_lock.grid(row=3, column=0, padx=10, pady=10, ipadx=40, ipady=20, sticky="ws")
		button_exit = customtkinter.CTkButton(base_frameR, text="خروج", command=close, corner_radius=20, width=60, font=("B nazanin", 40))
		button_exit.grid(row=3, column=1, padx=10, pady=10, ipadx=20, ipady=20, sticky="es")


		clock();

	else:
		passwd.delete(0, END)
		txt_label.configure(text="Password is wrong!", text_color="#972727")

#---------------------------------- Starting page ----------------------------------#

welcome_frame = customtkinter.CTkFrame(master=root)
welcome_frame.pack(expand=True, fill=BOTH)
welcome_frame.grid_columnconfigure(0, weight=1)
welcome_frame.grid_rowconfigure((0,1,2), weight=1)
txt_label = customtkinter.CTkLabel(welcome_frame, text="Please Enter your password :", font=("Comic Sans MS",70));
txt_label.grid(row=0, column=0, pady=(150,0))
passwd = customtkinter.CTkEntry(welcome_frame,  corner_radius=15, placeholder_text="password", font=("Comic Sans MS", 40), justify=CENTER, show="*")
passwd.grid(row=1, column=0, ipady=20, ipadx=50)
button_passwd = customtkinter.CTkButton(welcome_frame, text="Login", command=lambda: passcheck(Event), corner_radius=20, font=("Comic Sans MS",50, "bold"))
button_passwd.grid(row=2, column=0, ipady=50, ipadx=150, pady=(0,100))


root.bind("<Return>", passcheck);


root.mainloop();
