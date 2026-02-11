import hashlib
import time
import threading
from tkinter import *
from tkinter import ttk, filedialog, messagebox, scrolledtext
import itertools
import string
import os
import queue

class HashTool:
    def __init__(self, root):
        self.root = root
        self.root.title("Hash Tool v2.0")
        self.root.geometry("600x700")
        self.bg = "#2b2b2b"
        self.fg = "#ffffff"
        self.btn_color = "#007bff"
        self.root.configure(bg=self.bg)
        
        style = ttk.Style()
        style.theme_use('clam')
        
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(expand=True, fill='both', padx=5, pady=5)
        
        self.status = Label(self.root, text="Hazır", bg=self.bg, fg="#888", anchor=W)
        self.status.pack(side=BOTTOM, fill=X, padx=10, pady=5)

        self.create_cracker_tab(self.notebook)
        self.create_converter_tab(self.notebook)
        
        self.stop_flag = False
        self.log_queue = queue.Queue()
        self.process_log_queue()

    def create_cracker_tab(self, notebook):
        tab = Frame(notebook, bg=self.bg)
        notebook.add(tab, text="  🔓 Hash Cracker  ")
        
        Label(tab, text="Kırmak istediğiniz Hash:", 
              bg=self.bg, fg=self.fg, font=("Arial", 11)).pack(pady=10)
        
        self.crack_input = Entry(tab, font=("Consolas", 11), width=60)
        self.crack_input.pack(pady=5)
        
        type_frame = Frame(tab, bg=self.bg)
        type_frame.pack(pady=10)
        
        Label(type_frame, text="Hash Türü:", 
              bg=self.bg, fg=self.fg).pack(side=LEFT, padx=10)
        
        self.crack_type = ttk.Combobox(type_frame,
                                      values=["MD5", "SHA1", "SHA256"],
                                      state="readonly", width=15)
        self.crack_type.current(0)
        self.crack_type.pack(side=LEFT)
        
        Label(tab, text="Kırma Yöntemi:", 
              bg=self.bg, fg=self.fg, font=("Arial", 11)).pack(pady=15)
        
        self.method = StringVar(value="wordlist")
        
        method_frame = Frame(tab, bg=self.bg)
        method_frame.pack()
        
        Radiobutton(method_frame, text="📖 Wordlist (Sözlük)", 
                   variable=self.method, value="wordlist",
                   bg=self.bg, fg=self.fg, 
                   selectcolor="#444", activebackground=self.bg, activeforeground=self.fg).pack(anchor=W)
        
        Radiobutton(method_frame, text="💪 Brute Force (Kaba Kuvvet)", 
                   variable=self.method, value="brute",
                   bg=self.bg, fg=self.fg, 
                   selectcolor="#444", activebackground=self.bg, activeforeground=self.fg).pack(anchor=W)
        
        word_frame = Frame(tab, bg=self.bg)
        word_frame.pack(pady=10)
        
        Label(word_frame, text="Wordlist:", 
              bg=self.bg, fg=self.fg).pack(side=LEFT, padx=5)
        
        self.wordlist = Entry(word_frame, width=35, bg="#1e1e1e", fg=self.fg)
        self.wordlist.pack(side=LEFT, padx=5)
        
        if os.path.exists("wordlist.txt"):
            self.wordlist.insert(0, "wordlist.txt")
        
        Button(word_frame, text="Dosya Seç", 
               command=self.select_wordlist,
               bg="#4a4a4a", fg="white").pack(side=LEFT)
        
        brute_frame = Frame(tab, bg=self.bg)
        brute_frame.pack(pady=10)
        
        Label(brute_frame, text="Max Uzunluk:", 
              bg=self.bg, fg=self.fg).pack(side=LEFT, padx=5)
        
        self.max_len = Spinbox(brute_frame, from_=1, to=8, width=5)
        self.max_len.delete(0, END)
        self.max_len.insert(0, "4")
        self.max_len.pack(side=LEFT)
        
        btn_frame = Frame(tab, bg=self.bg)
        btn_frame.pack(pady=15)
        
        self.start_btn = Button(btn_frame, text="🚀 BAŞLAT", 
                               command=self.start_crack,
                               bg="#28a745", fg="white", 
                               font=("Arial", 12, "bold"),
                               padx=20, pady=5)
        self.start_btn.pack(side=LEFT, padx=5)
        
        self.stop_btn = Button(btn_frame, text="⛔ DURDUR", 
                              command=self.stop_crack,
                              bg="#dc3545", fg="white", 
                              font=("Arial", 12, "bold"),
                              padx=20, pady=5, state=DISABLED)
        self.stop_btn.pack(side=LEFT, padx=5)

        self.progress = scrolledtext.ScrolledText(tab, 
                                                 height=10, 
                                                 bg="#1e1e1e", 
                                                 fg="#00ff00",
                                                 font=("Consolas", 9))
        self.progress.pack(fill=BOTH, expand=True, padx=20, pady=10)

    def create_converter_tab(self, notebook):
        tab = Frame(notebook, bg=self.bg)
        notebook.add(tab, text="  🔄 Hash Converter  ")
        
        Label(tab, text="Metni buraya yazın:", 
              bg=self.bg, fg=self.fg, font=("Arial", 11)).pack(pady=10)
        
        self.conv_input = scrolledtext.ScrolledText(tab, height=4, 
                                                    bg="#1e1e1e", fg=self.fg,
                                                    font=("Arial", 11))
        self.conv_input.pack(fill=X, padx=20, pady=5)
        
        Button(tab, text="⚡ TÜM FORMATLARA DÖNÜŞTÜR", 
               command=self.convert_all,
               bg=self.btn_color, fg="white", 
               font=("Arial", 12, "bold"),
               cursor="hand2", padx=30, pady=10).pack(pady=15)
        
        Label(tab, text="Dönüştürülmüş Hash'ler (Tüm Formatlar):", 
              bg=self.bg, fg=self.fg, font=("Arial", 11)).pack()
        
        result_frame = Frame(tab, bg=self.bg)
        result_frame.pack(fill=BOTH, expand=True, padx=20, pady=10)
        
        self.conv_output = scrolledtext.ScrolledText(result_frame, 
                                                     bg="#1e1e1e", 
                                                     fg="#00ff00",
                                                     font=("Consolas", 10))
        self.conv_output.pack(fill=BOTH, expand=True)
        
        btn_frame = Frame(tab, bg=self.bg)
        btn_frame.pack(pady=5)
        
        Button(btn_frame, text="📋 Tümünü Kopyala", 
               command=self.copy_all_hashes,
               bg="#28a745", fg="white", 
               font=("Arial", 10)).pack(side=LEFT, padx=5)
        
        Button(btn_frame, text="🗑️ Temizle", 
               command=lambda: self.conv_output.delete("1.0", END),
               bg="#dc3545", fg="white", 
               font=("Arial", 10)).pack(side=LEFT, padx=5)

    def select_wordlist(self):
        filename = filedialog.askopenfilename(
            title="Wordlist Seç",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        if filename:
            self.wordlist.delete(0, END)
            self.wordlist.insert(0, filename)
    
    def start_crack(self):
        target = self.crack_input.get().strip().lower()
        
        if not target:
            messagebox.showwarning("Uyarı", "Lütfen bir hash girin!")
            return
        
        hash_type = self.crack_type.get().lower()
        expected_lengths = {"md5": 32, "sha1": 40, "sha256": 64}
        
        if len(target) != expected_lengths.get(hash_type, 0):
            messagebox.showerror("Hata", f"{hash_type.upper()} hash'i {expected_lengths[hash_type]} karakter olmalıdır!")
            return
        
        if not all(c in '0123456789abcdef' for c in target):
            messagebox.showerror("Hata", "Geçersiz hash formatı! Sadece hexadecimal karakterler (0-9, a-f) içermelidir.")
            return
        
        if self.method.get() == "wordlist":
            wordlist_file = self.wordlist.get()
            if not wordlist_file:
                messagebox.showwarning("Uyarı", "Lütfen wordlist seçin!")
                return
            if not os.path.exists(wordlist_file):
                messagebox.showerror("Hata", "Wordlist dosyası bulunamadı!")
                return
            if os.path.getsize(wordlist_file) > 100 * 1024 * 1024:
                if not messagebox.askyesno("Uyarı", "Wordlist dosyası çok büyük (>100MB). Devam edilsin mi?"):
                    return
        
        max_len = int(self.max_len.get())
        if self.method.get() == "brute" and max_len > 8:
            if not messagebox.askyesno("Uyarı", f"{max_len} karakter için brute force çok uzun sürebilir. Devam edilsin mi?"):
                return
        
        self.start_btn.config(state=DISABLED)
        self.stop_btn.config(state=NORMAL)
        self.stop_flag = False
        
        self.progress.delete("1.0", END)
        self.status.config(text="İşlem başlatıldı...")
        
        thread = threading.Thread(target=self.crack_thread, args=(target,))
        thread.daemon = True
        thread.start()
    
    def stop_crack(self):
        self.stop_flag = True
        self.log("⛔ Durdurma isteği gönderildi...")
        self.status.config(text="Durduruluyor...")
    
    def crack_thread(self, target_hash):
        try:
            hash_type = self.crack_type.get().lower()
            start_time = time.time()
            
            self.log(f"🎯 Hedef Hash: {target_hash}")
            self.log(f"📊 Hash Türü: {hash_type.upper()}")
            self.log("=" * 50)
            
            result = None
            if self.method.get() == "wordlist":
                result = self.wordlist_attack(target_hash, hash_type)
            else:
                result = self.brute_force_attack(target_hash, hash_type)
            
            elapsed = time.time() - start_time
            
            self.log("\n" + "=" * 50)
            if result:
                self.log(f"✅ BAŞARILI! Şifre: {result}")
                self.log(f"⏱️  Süre: {elapsed:.2f} saniye")
                self.status.config(text="Şifre Bulundu!")
                messagebox.showinfo("Başarılı!", f"Şifre bulundu!\n\n{result}")
            else:
                if self.stop_flag:
                    self.log("⛔ İşlem kullanıcı tarafından durduruldu.")
                    self.status.config(text="Durduruldu")
                else:
                    self.log(f"❌ Şifre bulunamadı")
                    self.status.config(text="Tamamlandı - Bulunamadı")
                self.log(f"⏱️  Süre: {elapsed:.2f} saniye")
                
        except Exception as e:
            self.log(f"❌ Hata: {str(e)}")
            self.status.config(text="Hata oluştu")
            messagebox.showerror("Hata", f"İşlem sırasında hata oluştu:\n{str(e)}")
        finally:
            self.root.after(0, lambda: self.start_btn.config(state=NORMAL))
            self.root.after(0, lambda: self.stop_btn.config(state=DISABLED))
    
    def wordlist_attack(self, target_hash, hash_type):
        wordlist_file = self.wordlist.get()
        self.log(f"📖 Wordlist: {wordlist_file}")
        
        try:
            file_size = os.path.getsize(wordlist_file)
            self.log(f"📦 Dosya boyutu: {file_size / 1024:.2f} KB")
            
            with open(wordlist_file, 'r', encoding='utf-8', errors='ignore') as f:
                self.log("🔄 Deneniyor...\n")
                
                attempts = 0
                for line in f:
                    if self.stop_flag:
                        return None
                    
                    word = line.strip()
                    if not word:
                        continue
                    
                    attempts += 1
                    
                    try:
                        if hash_type == "md5":
                            h = hashlib.md5(word.encode('utf-8')).hexdigest()
                        elif hash_type == "sha1":
                            h = hashlib.sha1(word.encode('utf-8')).hexdigest()
                        elif hash_type == "sha256":
                            h = hashlib.sha256(word.encode('utf-8')).hexdigest()
                        else:
                            continue
                    except Exception:
                        continue
                    
                    if attempts % 10000 == 0:
                        self.root.after(0, lambda a=attempts, w=word: self.status.config(text=f"Deneme: {a:,} - Son: {w[:20]}"))
                    
                    if h == target_hash:
                        self.log(f"\n🔍 Toplam deneme: {attempts:,}")
                        return word
                
                self.log(f"\n🔍 Toplam deneme: {attempts:,}")
                
        except MemoryError:
            self.log("❌ Bellek hatası: Dosya çok büyük!")
            messagebox.showerror("Hata", "Bellek yetersiz! Daha küçük bir wordlist kullanın.")
            return None
        except PermissionError:
            self.log(f"❌ Dosya erişim hatası: İzin reddedildi")
            messagebox.showerror("Hata", "Dosyaya erişim izni yok!")
            return None
        except Exception as e:
            self.log(f"❌ Dosya hatası: {str(e)}")
            return None
            
        return None
    
    def brute_force_attack(self, target_hash, hash_type):
        max_length = int(self.max_len.get())
        chars = string.ascii_lowercase + string.digits
        
        self.log(f"🔤 Karakterler: {chars}")
        self.log(f"📏 Max uzunluk: {max_length}")
        
        total_combinations = sum(len(chars) ** i for i in range(1, max_length + 1))
        self.log(f"🔢 Toplam kombinasyon: {total_combinations:,}")
        self.log("💪 Deneniyor...\n")
        
        attempts = 0
        
        for length in range(1, max_length + 1):
            if self.stop_flag:
                return None
            
            self.log(f"\n🔍 {length} basamaklı kombinasyonlar deneniyor...")
            self.status.config(text=f"{length} basamaklılar deneniyor...")
            
            for combo in itertools.product(chars, repeat=length):
                if self.stop_flag:
                    return None
                
                password = ''.join(combo)
                attempts += 1
                
                try:
                    if hash_type == "md5":
                        h = hashlib.md5(password.encode('utf-8')).hexdigest()
                    elif hash_type == "sha1":
                        h = hashlib.sha1(password.encode('utf-8')).hexdigest()
                    elif hash_type == "sha256":
                        h = hashlib.sha256(password.encode('utf-8')).hexdigest()
                    else:
                        continue
                except Exception:
                    continue
                
                if attempts % 50000 == 0:
                    progress = (attempts / total_combinations) * 100
                    self.root.after(0, lambda p=progress, pw=password: self.status.config(text=f"İlerleme: {p:.2f}% - Denenen: {pw}"))
                
                if h == target_hash:
                    self.log(f"\n🔍 Toplam deneme: {attempts:,}")
                    return password
        
        self.log(f"\n🔍 Toplam deneme: {attempts:,}")
        return None
    
    def log(self, message):
        self.log_queue.put(message)
    
    def process_log_queue(self):
        try:
            while True:
                message = self.log_queue.get_nowait()
                self.progress.insert(END, message + "\n")
                self.progress.see(END)
        except queue.Empty:
            pass
        finally:
            self.root.after(100, self.process_log_queue)

    def convert_all(self):
        text = self.conv_input.get("1.0", END).strip()
        
        if not text:
            messagebox.showwarning("Uyarı", "Lütfen metin yazın!")
            return
        
        if len(text) > 1000000:
            messagebox.showerror("Hata", "Metin çok uzun! Maksimum 1MB metin işlenebilir.")
            return
        
        self.conv_output.delete("1.0", END)
        self.status.config(text="Hash'ler oluşturuluyor...")
        
        self.conv_output.insert(END, "="*80 + "\n")
        self.conv_output.insert(END, f"  METIN: {text[:100]}{'...' if len(text) > 100 else ''}\n")
        self.conv_output.insert(END, f"  UZUNLUK: {len(text)} karakter\n")
        self.conv_output.insert(END, "="*80 + "\n\n")
        
        algorithms = {
            'MD5': hashlib.md5,
            'SHA1': hashlib.sha1,
            'SHA224': hashlib.sha224,
            'SHA256': hashlib.sha256,
            'SHA384': hashlib.sha384,
            'SHA512': hashlib.sha512,
        }
        
        try:
            algorithms['SHA3-256'] = hashlib.sha3_256
            algorithms['SHA3-512'] = hashlib.sha3_512
        except AttributeError:
            pass
        
        try:
            algorithms['BLAKE2b'] = hashlib.blake2b
            algorithms['BLAKE2s'] = hashlib.blake2s
        except AttributeError:
            pass
        
        success_count = 0
        
        for algo_name, algo_func in algorithms.items():
            try:
                h = algo_func()
                h.update(text.encode('utf-8'))
                hash_value = h.hexdigest()
                
                self.conv_output.insert(END, f"┌─ {algo_name} ".ljust(80, '─') + "\n")
                self.conv_output.insert(END, f"│ {hash_value}\n")
                self.conv_output.insert(END, f"│ Uzunluk: {len(hash_value)} karakter\n")
                self.conv_output.insert(END, "└" + "─"*79 + "\n\n")
                
                success_count += 1
                
            except Exception as e:
                self.conv_output.insert(END, f"┌─ {algo_name} ".ljust(80, '─') + "\n")
                self.conv_output.insert(END, f"│ Hata: {str(e)}\n")
                self.conv_output.insert(END, "└" + "─"*79 + "\n\n")
        
        self.conv_output.insert(END, "\n" + "="*80 + "\n")
        self.conv_output.insert(END, f"  Toplam {success_count} farklı formatta hash oluşturuldu!\n")
        self.conv_output.insert(END, "="*80 + "\n")
        
        self.status.config(text=f"Tamamlandı: {success_count} hash oluşturuldu.")

    def copy_all_hashes(self):
        text = self.conv_output.get("1.0", END).strip()
        if not text:
            messagebox.showwarning("Uyarı", "Kopyalanacak hash yok!")
            return
        
        try:
            self.root.clipboard_clear()
            self.root.clipboard_append(text)
            messagebox.showinfo("Başarılı", "Tüm hash'ler kopyalandı!")
        except Exception as e:
            messagebox.showerror("Hata", f"Kopyalama hatası: {str(e)}")

if __name__ == "__main__":
    root = Tk()
    app = HashTool(root)
    root.mainloop()