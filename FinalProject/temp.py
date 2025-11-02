import matplotlib.pyplot as plt
import seaborn as sns

# 設定 Matplotlib 樣式以獲得更好的視覺效果
sns.set_theme(style="whitegrid")

# 設置中文顯示 (如果您的環境需要)
# plt.rcParams['font.sans-serif'] = ['Microsoft YaHei'] # 替換為您系統支援的中文字體
# plt.rcParams['axes.unicode_minus'] = False 

# --- 圖表一: X軸為小時, Y軸為平均花費時間 ---
plt.figure(figsize=(12, 6))
sns.lineplot(data=df_avg_time, 
             x='hour', 
             y='平均花費時間 (秒)', 
             hue='執行方法', 
             marker='o', 
             palette='viridis')

plt.title('🚀 不同執行方法在各小時的平均花費時間', fontsize=16)
plt.xlabel('小時 (0-23)', fontsize=12)
plt.ylabel('平均花費時間 (秒)', fontsize=12)
plt.xticks(range(0, 24)) # 確保X軸顯示所有小時
plt.legend(title='執行方法')
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()

# --- 圖表二: X軸為小時, Y軸為 all method 的呼叫次數 (總量) ---
plt.figure(figsize=(12, 6))
# 使用 Bar Plot 可以更好地表示次數的總和
sns.barplot(data=df_call_count, 
            x='hour', 
            y='呼叫次數', 
            palette='Reds_d')

plt.title('📈 All Method 在各小時的呼叫總次數 (監測尖峰期)', fontsize=16)
plt.xlabel('小時 (0-23)', fontsize=12)
plt.ylabel('呼叫次數', fontsize=12)
plt.xticks(range(0, 24))
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()
