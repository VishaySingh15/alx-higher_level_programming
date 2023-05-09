#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current_ptr = *head, *temp_node;

	if (!number)
		return (NULL);

	while (current_ptr != NULL)
	{
		if (number < current_ptr->n)
		{
			temp_node->n = number;
			temp_node->next = current_ptr->next;
			current_ptr->next = temp_node;
			return (current_pointer->next);
		}
		current_ptr = current_ptr->next;
	}

	return (NULL);
}
