from tkinter import* 
import tkinter as tk 
import tkinter.ttk as ttk
from tkinter.ttk import*


def  __init__ ( öz ,  kazan ):
        
        öz . labelUrun  =  tk . Etiket ( app ,  text = "Ürün Seçin" ) 
        öz . labelUrun . ızgara ( sütun = 0 ,  satır = 0 )

        öz . urun  =  ttk . Combobox ( 
            app ,  değerler = [ "Yüzük" ,  "Kolye" ,  "Bilezik" ],  durum = "salt okunur" 
        )

        öz . urun . ızgara ( sütun = 1 ,  satır = 0 ) 
        öz . urun . akım ( 0 )

        öz . labelAyar  =  tk . Etiket ( uygulama ,  metin = "Ayar Seçin" ) 
        kendisi . etiketAyar . ızgara ( sütun = 0 ,  satır = 1 )

        öz . ayar  =  ttk . Combobox ( uygulama ,  değerler = [ "14" ,  "22" ],  durum = "salt okunur" )

        öz . ayar . ızgara ( sütun = 1 ,  satır = 1 ) 
        öz . ayar . akım ( 0 )

        öz . labelGram  =  tk . Etiket ( uygulama ,  metin = "Gramaj Girin" ) 
        öz . labelGram . ızgara ( sütun = 0 ,  satır = 2 )

        öz . gram  =  Giriş ( uygulama ) 
        öz . gram . ızgara ( sütun = 1 ,  satır = 2 )

        öz . gönder  =  Düğme ( app ,  text = "Hesapla" ,  command = self . hesapla ) 
        self . gönder . ızgara ( sütun = 0 ,  satır = 3 )

        öz . lableSonuc  =  tk . Etiket ( uygulama ,  metin = "Sonuç" ) 
        öz . lableSonuc . ızgara ( sütun = 0 ,  satır = 4 )

        öz . sonuc  =  Giriş ( uygulama ) 
        self . sonuc . ızgara ( sütun = 1 ,  satır = 4 )

def  hesapla ( öz ): 
        öz . sonuc . sil ( 0 ,  "son" )

        eğer  öz . urun . get ()  ==  "Yüzük" : 
            eğer  öz . ayar . get ()  ==  "14" : 
                öz . sonuc . insert ( END ,  str ( round ( 350  *  int ( self . gram . get ())  *  1.18 ,  3 ))) 
        else : 
                self . sonuc . ekle (END ,  str ( round ( 450  *  int ( self . Gram . Get ())  *  1.18 ,  3 )))

        elif  öz . urun . get ()  ==  "Bilezik" : 
            eğer  kendinden ise . ayar . get ()  ==  "14" : 
                öz . sonuc . insert ( END ,  str ( round ( 400  *  int ( self . gram . get ())  *  1.18 ,  3 ))) 
        else : 
                self . sonuc . ekle (END ,  str ( round ( 500  *  int ( self . Gram . Get ())  *  1.18 ,  3 ))) 
        else : 
            eğer  self . ayar . get ()  ==  "14" : 
                öz . sonuc . ekle ( END ,  str ( round ( 380  *  int ( self . gram . get ()) *  1.18 ,  3 ))) 
            başka : 
                öz . sonuc . ekle ( END ,  str ( round ( 480  *  int ( self . gram . get ())  *  1.18 ,  3 )))


app  =  tk . Tk () 
uygulaması . geometri ( "300x200" ) 
mywin  =  Kuyumcu ( uygulama )

app . başlık ( "Kuyumcu" )

app . ana döngü ()
Metin olarak indir
