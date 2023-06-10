#include "lists.h"

/**
 * insert_node - start point
 * @head: input
 * @number: input
 *
 * Return: listint_t
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *comp, *new_node, *reset;
	int i = 0;

	reset = *head;
	comp = *head;
	new_node = malloc(sizeof(listint_t));
	new_node->n = number;
	while(*head->next)
	{
		if (comp->n < new_node->n)
		{
			if (i == 0)
			{
				new_node->next = *head, *head = new_node;
				return (*head);
			}
			else
			{
				new_node->next = *head;
				comp->next = new_node;
				*head = reset;
				return (*head);
			}
		}
		if (i == 0)
			*head = **head->next;
		i++;
		*head = **head->next;
		comp = comp->next;
	}
	new_node->next = **head->next;
	**head->next = new_node;
	*head = reset;
	return (*head);
}

