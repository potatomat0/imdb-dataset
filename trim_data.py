import pandas as pd


def trim_text(text, max_length=4800):
  """Hàm này cắt ngắn văn bản xuống độ dài tối đa, 
  nếu vượt quá sẽ thêm dấu ba chấm (...) báo hiệu phần bị cắt.

  Args:
      text: Văn bản cần cắt (chuỗi).
      max_length: Độ dài tối đa của văn bản (mặc định: 4800 ký tự).

  Returns:
      str: Văn bản đã được cắt ngắn.
  """
  if len(text) > max_length:
    return text[:max_length] + "..."
  else:
    return text


def sentiment_to_comment(sentiment):
  """Hàm này chuyển đổi sentiment (0 hoặc 1) thành 
  một bình luận với phần mở đầu phụ thuộc vào sentiment.

  Args:
      sentiment: Giá trị sentiment (0 hoặc 1).

  Returns:
      str: Chuỗi bình luận với phần mở đầu phụ thuộc sentiment.
  """
  if sentiment == 1:
    return "Tôi thích bộ phim này..."
  else:
    return "Tôi không thích bộ phim này..."


# Đọc dữ liệu đã xử lý
df = pd.read_csv("processed_dataset.csv")

# Cắt ngắn text review (tùy chọn)
df["review"] = df["review"].apply(trim_text)

# Giới hạn dữ liệu xuống 500 dòng đầu (tùy chọn)
df = df.head(500)

# Thêm cột comment dựa trên sentiment
df["comment"] = df["sentiment_numeric"].apply(sentiment_to_comment)

# Lưu dữ liệu đã cắt ngắn
df.to_csv("trimmed_data.csv", index=False)

# In ra DataFrame (tùy chọn)
print(df)
