def cleanDataByClassName(data, className):
    """Clean data by class name.

    Args:
        data (eTree._Element): The HTML to be parsed.
        className (str): Class name.

    Returns:
        Cleaned data as a string to be placed in a csv cell.
    """
    
    if className == 'portstable':

        output = ""

        children = data.findChildren('tr')
        for i, child in enumerate(children):

            # Get the text of the child
            child_text = child.text
            # Get the td children
            td_child = child.findChildren('td')
            td = td_child[1]

            # Get the value of the input
            input = td.findChildren('input')
            value = input[0].get('value')

            # Format the output
            if i < len(children) - 1:
                output += child_text + ": " + value + ", "
            else:
                output += child_text + ": " + value
        return output
    elif className == 'productstandardstable':
        output = ""
        rows = data.findChildren('tr')
        for i, row in enumerate(rows):
            if i == 0:
                # Get th children
                th_children = row.findChildren('th')
                output += f"({th_children[0].text},{th_children[1].text}): "
            elif i > 0 and i < len(rows) - 1:
                # Get td children, leave off first element
                td_children = row.findChildren('td')[1:]
                output += f"({td_children[0].text},{td_children[1].text}), "
            else:
                # Get td children, leave off first element
                td_children = row.findChildren('td')[1:]
                output += f"({td_children[0].text},{td_children[1].text})"

        return output

def cleanDataByXpath(data, xpath):
    """Clean data by xpath.

    Args:
        data (eTree._Element): The HTML to be parsed.
        xpath (str): Xpath.

    Returns:
        Cleaned data as a string to be placed in a csv cell.
    """

    if xpath == "/html/body/div[2]/div/div/form/div/div[3]/div[2]/div[2]/div[2]/table[1]":

        checked_list = []

        # Get the table's children
        children = data.xpath(xpath)[0].iterchildren()
        tr_list = list(list(children)[0].iterchildren())
        for tr in tr_list:
            td_list = list(tr.iterchildren())
            for td in td_list:

                checked = False

                # Get the inputs
                input_list = list(td.iterchildren())
                for input in input_list:
                    if input.get('type') == 'checkbox':
                        if input.get('checked') == 'checked':
                            checked = True
                        else:
                            continue

                if checked:
                    # Get the text of the input with type = text
                    for input in input_list:
                        if input.get('type') == 'text':
                            checked_list.append(input.get('value'))
                            break

        return ", ".join(checked_list)