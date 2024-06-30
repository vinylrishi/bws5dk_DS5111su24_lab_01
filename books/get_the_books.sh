while read -r url; do
	wget "$url"
done < test_books.txt
