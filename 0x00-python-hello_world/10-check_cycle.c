#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: pointer to the head of the list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *temp, *reset;

	temp = list;
	reset = list;
	list = list->next;
	while (list)
	{
		list = list->next;
		if (list == temp)
			return (1);
		temp = temp->next;
	}
	list = reset;
	return (0);
}
