import yt_dlp
import os


def yt():
    link = input("Enter the link of video you would like to download.\n")
    output_file = input("Enter the name of the output file.").strip()
    if not link:
        print("You can't leave this empty")
        return

    # full_output = os.path.join(output_file)

    if not output_file.endswith(".mp4"):
        output_file += ".mp4"
# print(f"No output path provided. Defaulting to: {output_path}")

    ydl_opts = {
        'outtmpl': output_file}
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([f'{link}', output_file])
        print("✅ Download Completed ✅")
    except Exception as e:
        print(f"⚠️ Download failed: {e}")


def insta():
    link = input(
        "Enter the link of video you would like to download.\n").strip()
    output_file = input("Enter the name of the output file.").strip()
    if not link:
        print("You can't leave this empty")
        return
    if not output_file.endswith(".mp4"):
        output_file += ".mp4"
    ydl_opts = {'cookies': 'cookies.txt',
                'outtmpl': output_file}
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([f'{link}'])
        print("✅ Download Completed ✅")
    except Exception as e:
        print(f"⚠️ Download failed: {e}")


def main():

    choice = int(input("Enter 1 for yt and 2 for insta."))

    is_running = True
    while is_running:
        if choice == 1:
            yt()
            is_running = False
        elif choice == 2:
            insta()
            is_running = False
        elif choice == 3:
            is_running = False
        else:
            break


if __name__ == '__main__':
    main()
