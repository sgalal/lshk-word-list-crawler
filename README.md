# lshk-word-list-crawler

Crawler for Cantonese pronunciation data on [LSHK Jyutping Word List](https://corpus.eduhk.hk/JPwordlist/) (香港語言學學會粵拼詞表)

See `sanitized.txt` for the final result.

## File structure

* `lshk.py`: The crawler
* `result.txt`: Raw result output by the crawler
* `sanitize.py`: Sanitizer for the result
* `sanitized.txt`: Final result output by the sanitizer
* `sanitize_log.txt`: Sanitize log

## License

According to the original terms, the dictionary data is distributed under **CC BY 4.0**.

Python code in this repository is distributed under MIT license.

## Disclaimer

This repository is only for the collection of the dictionary data. The owner of this repository does not contribute to the word list itself. To the knowledge of the owner of this repository, the data is not fully accurate.

The link of the word list is now broken. If you are interested in a more up-to-date word list, see [rime/rime-cantonese](https://github.com/rime/rime-cantonese).
