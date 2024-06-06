while read -r url; do
	wget "$url"
done < book_texts.txt
