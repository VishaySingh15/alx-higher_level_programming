#include "lists.h"
#include <stdlib.h>
/**
 * insert_node - inputs a node
 * @head: pointer to the first node
 * @number: integer to input
 * Return: NULL if fails and pointer if success
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current_ptr, *prev_ptr, *temp_node = malloc(sizeof(listint_t));

	if (!number)
	{
		free(temp_node);
		return (NULL);
	}
	if (!*head)
	{
		temp_node->n = number;
		temp_node->next = NULL;
		*head = temp_node;
		return (temp_node);
	}

	if (number < (*head)->n)
	{
		temp_node->n = number;
		temp_node->next = *head;
		*head = temp_node;
		return (temp_node);
	}

	current_ptr = (*head)->next;
	prev_ptr = *head;

	while (current_ptr != NULL)
	{
		if (number < current_ptr->n)
		{
			temp_node->n = number;
			temp_node->next = current_ptr;
			prev_ptr->next = temp_node;
			return (temp_node);
		}
		prev_ptr = current_ptr;
		current_ptr = current_ptr->next;
	}

	temp_node->n = number;
	temp_node->next = NULL;
	current_ptr->next = temp_node;
	return (temp_node);
}
