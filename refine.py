import pandas as pd

# Đọc dữ liệu CSV vào một DataFrame
df = pd.read_csv("dataset.csv")

# Định nghĩa hàm chuyển đổi sentiment thành giá trị số (0 hoặc 1)
def sentiment_to_numeric(sentiment):
  """Hàm này chuyển đổi sentiment (tích cực hoặc tiêu cực) thành giá trị số.

  Args:
      sentiment: Chuỗi biểu thị sentiment của một đánh giá phim (vd: "positive" hoặc "negative").

  Returns:
      int: 1 nếu sentiment là tích cực, 0 nếu sentiment là tiêu cực.

  Raises:
      ValueError: Nếu sentiment không phải "positive" hoặc "negative".
  """
  if sentiment == "positive":
    return 1
  elif sentiment == "negative":
    return 0
  else:
    # Xử lý trường hợp sentiment không phải "positive" hoặc "negative" (tùy chọn)
    # Bạn có thể raise lỗi, gán giá trị mặc định, ...
    raise ValueError(f"Sentiment không hợp lệ: {sentiment}")

# Thêm cột 'sentiment_numeric' mới với giá trị chuyển đổi từ cột A
df["sentiment_numeric"] = df["sentiment"].apply(sentiment_to_numeric)

# Xóa cột 'sentiment' cũ
del df["sentiment"]

# Thêm cột 'ID' với giá trị bằng index của mỗi dòng (sau cùng)
df["ID"] = df.index

# Chuyển đổi vị trí cột (tùy chọn, có thể bỏ qua)
# df = df[['review', 'sentiment_numeric', 'ID']]

# Lưu dữ liệu đã xử lý vào file CSV mới (tùy chọn)
df.to_csv("processed_data.csv", index=False)

# In ra DataFrame đã xử lý (tùy chọn)
print(df)
