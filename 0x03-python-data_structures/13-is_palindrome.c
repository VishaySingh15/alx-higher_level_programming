#include "lists.h"
/**
 * is_palindrome - determines if list is a palindrome
 * @head: pointer to first list item
 * Return: 1 if palindrome, 0 if not
 */
int is_palindrome(listint_t **head)
{
	int length = 0, count = 0, result;
	listint_t *cur_ptr;

	if (!*head)
	{
		return (1);
	}
	cur_ptr = *head;
	while (cur_ptr != NULL)
	{
		cur_ptr = cur_ptr->next;
		length++;
	}
	while (count < (length + 1) / 2)
	{
		result = get_int(count, length - 1 - count, *head);
		if (!result)
		{
			return (0);
		}
		count++;
	}
	return (1);
}

/**
 * get_int - returns int at list index
 * @idx: index
 * @ptr: pointer to first list item
 * Return: int at index
 */
int get_int(int idx1, int idx2, listint_t *ptr)
{
	int count = 0, beg, end;

	while (count != idx1)
	{
		ptr = ptr->next;
		count++;
	}
	beg = ptr->n;
	while (count != idx2)
        {
                ptr = ptr->next;
                count++;
        }
	end = ptr->n;
	return (beg == end);
}
