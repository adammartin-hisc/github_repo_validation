import csv
import json


def format_output(repositories, file_format, file_name):
    with open(_full_file_name(file_name, file_format), 'w') as output:
        if file_format == 'csv':
            _write_csv(output, repositories)
        _write_jsonl(output, repositories)


def _write_csv(output, repositories):
    fieldnames = repositories[0].keys()
    writer = csv.DictWriter(output, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(repositories)


def _write_jsonl(output, repositories):
    for entry in repositories:
        output.writelines(json.dumps(entry)+'\n')


def _full_file_name(file_name, file_format):
    return file_name + '.' + file_format