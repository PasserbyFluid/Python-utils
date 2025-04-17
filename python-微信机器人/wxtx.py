from PIL import Image, ImageDraw, ImageFont

def create_chat_screenshot(chat_data, output_file="chat_screenshot.png"):
  """
  生成微信聊天记录截图
  :param chat_data: 聊天内容列表，每项为字典，包含 'sender' 和 'message'
  :param output_file: 输出文件名
  """
  # 设置图片宽高和背景颜色
  img_width = 500
  img_height = 100 + len(chat_data) * 80
  background_color = (255, 255, 255)  # 白色背景

  # 创建图片
  img = Image.new("RGB", (img_width, img_height), background_color)
  draw = ImageDraw.Draw(img)

  # 加载字体
  try:
    font = ImageFont.truetype("arial.ttf", 16)  # 替换为系统中的字体路径
  except IOError:
    font = ImageFont.load_default()

  # 定义聊天气泡样式
  bubble_padding = 10
  bubble_margin = 20
  text_color = (0, 0, 0)  # 黑色文字
  sender_color = (220, 248, 198)  # 发送方气泡颜色（绿色）
  receiver_color = (255, 255, 255)  # 接收方气泡颜色（白色）
  border_color = (200, 200, 200)  # 气泡边框颜色

  y_offset = 20  # 初始 Y 轴偏移量

  for chat in chat_data:
    sender = chat["sender"]
    message = chat["message"]

    # 计算文字大小
    text_size = font.getsize(message)  # 使用 font.getsize 替代 draw.textsize
    bubble_width = text_size[0] + bubble_padding * 2
    bubble_height = text_size[1] + bubble_padding * 2

    if sender == "me":  # 发送方
      bubble_x = img_width - bubble_width - bubble_margin
      bubble_color = sender_color
    else:  # 接收方
      bubble_x = bubble_margin
      bubble_color = receiver_color

    # 绘制气泡
    bubble_y = y_offset
    draw.rectangle(
      [bubble_x, bubble_y, bubble_x + bubble_width, bubble_y + bubble_height],
      fill=bubble_color,
      outline=border_color,
    )

    # 绘制文字
    text_x = bubble_x + bubble_padding
    text_y = bubble_y + bubble_padding
    draw.text((text_x, text_y), message, fill=text_color, font=font)

    # 更新 Y 轴偏移量
    y_offset += bubble_height + 10

  # 保存图片
  img.save(output_file)
  print(f"聊天截图已保存为 {output_file}")

# 你可以修改这个列表来设置不同的聊天内容
chat_data = [
  {"sender": "me", "message": "你好！这是一个测试消息。"},
  {"sender": "other", "message": "你好！收到你的消息了。"},
  {"sender": "me", "message": "这个工具可以生成微信聊天截图！"},
  {"sender": "other", "message": "太棒了！"},
]

# 生成聊天截图
create_chat_screenshot(chat_data)
